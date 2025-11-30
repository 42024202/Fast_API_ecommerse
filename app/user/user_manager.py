from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin
from app.user.models.user import User
from app.core.db_helpers import db_helper
from app.core.config import settings


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.secret_key
    verification_token_secret = settings.secret_key


async def get_user_manager(user_db=Depends(db_helper.user_db_depandancy)):
    yield UserManager(user_db)

