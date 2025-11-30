from contextlib import asynccontextmanager
from fastapi import FastAPI
from .core.config import settings

from .api.v1.product import router as product_router_v1
from .api.v1.refresh import router as refresh_router
from .api.v1.login import router as login_router
from .api.v1.user import router as user_router

from app.user.services import fastapi_users
from app.user.schemas.schema_v1 import UserRead, UserCreate, UserUpdate
from app.core.auth import auth_backend



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


"""PRODUCT ROUTERS"""
app.include_router(product_router_v1, prefix=f"{settings.api_v1_prefix}")


"""USER ROUTERs"""

"""user admin routers"""
app.include_router(user_router, prefix=f"{settings.api_v1_prefix}")

"""auth backend"""
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
    )

"""email verification router"""
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"]
    )

"""register routers"""
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
    )

"""login router"""
app.include_router(
    login_router,
    prefix="/auth",
    tags=["auth"]
    )

"""refresh router"""
app.include_router(
    refresh_router,
    prefix="/auth",
    tags=["auth"]
    )

"""user endpoints"""
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"]
    )

