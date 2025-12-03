from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.characters_crud import StorageCRUD
from app.phone.models import Storage
from app.phone.schemas_v1.characters.storage import StorageCreate, StorageUpdate


class StorageService:
    def __init__(self, crud: StorageCRUD):
        self.crud = crud

    async def create(
        self,
        session: AsyncSession,
        storage_in: StorageCreate,) -> Storage:

        return await self.crud.create_storage(session, storage_in)

    async def get_or_404(
        self,
        session: AsyncSession,
        storage_id: int) -> Storage:
        storage = await self.crud.get_storage(session, storage_id)
        if storage is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Storage not found")

        return storage

    async def storage_list(
        self,
        session: AsyncSession) -> list[Storage]:

        return await self.crud.get_storages(session)

    async def update_storage(
        self,
        session: AsyncSession,
        storage_id: int,
        storage_in: StorageUpdate) -> Storage:
        storage = await self.get_or_404(session, storage_id)
        updated = await self.crud.update_storage(session, storage, storage_in)

        return updated

    async def delete_storage(
        self,
        session: AsyncSession,
        storage_id: int):
        storage = await self.get_or_404(session, storage_id)
        await self.crud.delete_storage(session, storage)

        return {"detail": "Storage deleted"}


storage_service = StorageService(StorageCRUD())

