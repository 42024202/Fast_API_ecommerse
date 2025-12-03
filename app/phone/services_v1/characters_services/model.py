from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.characters_crud import ModelCRUD
from app.phone.models import Model
from app.phone.schemas_v1.characters import ModelCreate, ModelUpdate

model_crud = ModelCRUD()


class ModelService:
    def __init__(self, crud: ModelCRUD):
        self.crud = crud
    
    async def create(
        self,
        session: AsyncSession,
        model_in: ModelCreate,
        ) -> Model:

        return await self.crud.create_model(
                session,
                model_in)

    async def get_or_404(
        self,
        session: AsyncSession,
        model_id: int
        ) -> Model:

        model = await self.crud.get_model(session, model_id)
        if not model:
            raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Model not found")

        return model

    async def model_list(
        self,
        session: AsyncSession
        ) -> list[Model]:

        return await self.crud.get_models(session)

    async def update_model(
        self,
        session: AsyncSession,
        model_id: int,
        model_in: ModelUpdate
        ) -> Model:

        model = await self.get_or_404(session, model_id)
        updated = await self.crud.update_model(
                session=session,
                model=model,
                model_in=model_in
                )
        return updated

    async def delete_model(
        self,
        session: AsyncSession,
        model_id: int
        ):
        model = await self.get_or_404(session, model_id)
        await self.crud.delete_model(session, model)

        return {"detail": "Model deleted"}


model_service = ModelService(crud=model_crud)
