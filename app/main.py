from contextlib import asynccontextmanager
from fastapi import FastAPI, Path
from .core import db_helper, Base
from core.config import settings
from .api.v1.routers import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=f"{settings.api_v1_prefix}")

