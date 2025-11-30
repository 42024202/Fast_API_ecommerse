from fastapi import APIRouter, Depends
from fastapi_users.authentication import CookieTransport, JWTStrategy
from fastapi_users import FastAPIUsers
from fastapi import HTTPException

from app.core.auth import get_access_strategy, get_refresh_strategy
from app.user.user_manager import get_user_manager

router = APIRouter()


@router.post("/auth/jwt/login")
async def login(
    credentials: dict,
    user_manager=Depends(get_user_manager),
    access_strategy: JWTStrategy = Depends(get_access_strategy),
    refresh_strategy: JWTStrategy = Depends(get_refresh_strategy),
        ):

    user = await user_manager.authenticate(credentials)

    if user is None:
        raise HTTPException(400, "Invalid credentials")

    if not user.is_verified:
        raise HTTPException(403, "Email is not verified")

    access = await access_strategy.write_token({"sub": str(user.id), "aud": "access"})
    refresh = await refresh_strategy.write_token({"sub": str(user.id), "aud": "refresh"})

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
            }
