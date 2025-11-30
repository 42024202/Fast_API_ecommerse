from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from .core.config import settings
from .api.v1.product import router as product_router_v1

from app.user.services import fastapi_users
from app.core.auth import auth_backend
from app.user.schemas.schema_v1 import UserRead, UserCreate, UserUpdate


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

#== product routers ==
app.include_router(product_router_v1, prefix=f"{settings.api_v1_prefix}")

#== AUTH ROUTES ==
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"]
)

