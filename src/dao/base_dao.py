import uuid
from typing import Type, TypeVar, Optional, Sequence, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.logger import logger

T = TypeVar("T")


class BaseDAO:
    model: Type[T] = None

    @classmethod
    async def find_by_id(cls, db: AsyncSession, _id: uuid.UUID) -> Optional[T]:
        result = await db.execute(select(cls.model).where(cls.model.id == id))
        return result.scalars().first()

    @classmethod
    async def find_one_or_none(cls, db: AsyncSession, **_filter) -> Optional[T]:
        query = select(cls.model).filter_by(**_filter)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, db: AsyncSession, **filter_by) -> Sequence[T]:
        query = select(cls.model).filter_by(**filter_by)
        result = await db.execute(query)
        return result.scalars().all()

    @classmethod
    async def insert_one(cls, db: AsyncSession, obj: Any) -> Optional[T]:
        try:
            db.add(obj)
            await db.commit()
            await db.refresh(obj)
            logger.info(f"Inserted new {cls.model.__name__} with ID: {obj.id}")
            return obj
        except IntegrityError as e:
            await db.rollback()
            logger.error(f"IntegrityError while inserting {cls.model.__name__}: {e}")
            return None
