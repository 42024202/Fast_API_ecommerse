from fastapi import APIRouter, Depends, HTTPException
from fastapi_users.jwt import decode_jwt
from fastapi_users.authentication import JWTStrategy

from app.core.auth import get_access_strategy, get_refresh_strategy

router = APIRouter()


@router.post("/auth/jwt/refresh")
async def refresh_token(
    refresh_token: str,
    refresh_strategy: JWTStrategy = Depends(get_refresh_strategy),
    access_strategy: JWTStrategy = Depends(get_access_strategy),
        ):
    try:
        payload = decode_jwt(refresh_token, refresh_strategy.secret, audience="refresh")
    except Exception:
        raise HTTPException(401, "Invalid refresh token")

    user_id = payload["sub"]

    access = await access_strategy.write_token({"sub": user_id, "aud": "access"})
    return {"access_token": access, "token_type": "bearer"}
