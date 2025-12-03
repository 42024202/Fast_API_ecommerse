from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.phone.models import Storage
from app.phone.schemas_v1.characters.storage import StorageCreate, StorageUpdate


class StorageCRUD:

    async def create_storage(
            self,
            session: AsyncSession,
            storage_in: StorageCreate) -> Storage:

        storage = Storage(**storage_in.model_dump())
        session.add(storage)
        await session.commit()
        await session.refresh(storage)
        return storage

    async def get_storage(
            self,
            session: AsyncSession,
            storage_id: int) -> Storage | None:

        return await session.get(Storage, storage_id)

    async def get_storages(
            self,
            session: AsyncSession) -> list[Storage]:

        stmt = select(Storage).order_by(Storage.id)
        result: Result = await session.execute(stmt)
        storages = result.scalars().all()
        return list(storages)

    async def update_storage(
            self,
            session: AsyncSession,
            storage: Storage,
            storage_in: StorageUpdate) -> Storage:

        update_data = storage_in.model_dump(exclude_unset=True)
        for name, value in update_data.items():
            setattr(storage, name, value)

        await session.commit()
        await session.refresh(storage)
        return storage

    async def delete_storage(
            self,
            session: AsyncSession,
            storage: Storage):

        await session.delete(storage)
        await session.commit()

