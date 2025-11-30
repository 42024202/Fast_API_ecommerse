from fastapi_users import FastAPIUsers
from app.user.user_manager import get_user_manager
from app.core.auth import auth_backend
from app.user.models.user import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

