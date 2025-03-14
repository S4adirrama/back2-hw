from src.models.user import User

from src.dao.base_dao import BaseDAO


class UserDAO(BaseDAO):
    model = User
