from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.dao.user_dao import UserDAO
from src.models import User
from src.schemas.user import UserSignUpDTO


class UserRepository:
    @staticmethod
    async def create_user(user_data: UserSignUpDTO, db: AsyncSession) -> Optional[User]:
        new_user = User.create_user(user_data)
        return await UserDAO.insert_one(db, new_user)

    @staticmethod
    async def get_user_by_email(email: str, db: AsyncSession) -> Optional[User]:
        return await UserDAO.find_one_or_none(db, email=email)
