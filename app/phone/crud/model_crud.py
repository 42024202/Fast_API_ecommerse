from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.phone.models import Model
from app.phone.schemas_v1.characters.model import ModelCreate, ModelUpdate


class ModelCRUD:

    async def create_model(
                self,
                session: AsyncSession,
                model_in: ModelCreate
            ) -> Model:

        model = Model(**model_in.model_dump())
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return model

    async def get_model(
                self,
                session: AsyncSession,
                model_id: int
            ) -> Model | None:

        return await session.get(Model, model_id)

    async def get_models(
                self,
                session: AsyncSession
            ) -> list[Model]:

        stmt = select(Model).order_by(Model.id)
        result: Result = await session.execute(stmt)
        models = result.scalars().all()
        return list(models)

    async def update_model(
                self,
                session: AsyncSession,
                model: Model,
                model_in: ModelUpdate
            ) -> Model:

        update_data = model_in.model_dump(exclude_unset=True)

        for name, value in update_data.items():
            setattr(model, name, value)

        await session.commit()
        await session.refresh(model)
        return model

    async def delete_model(
                self,
                session: AsyncSession,
                model: Model
            ):

        await session.delete(model)
        await session.commit()

