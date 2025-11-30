from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from app.core.config import settings


bearer_transport = BearerTransport(tokenUrl="/auth/jwt/login")


def get_access_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.secret_key,
        lifetime_seconds=15 * 60,
        token_audience=["access"],
    )


def get_refresh_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.secret_key,
        lifetime_seconds=60 * 60 * 24 * 3,
        token_audience=["refresh"],
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_access_strategy,
)

