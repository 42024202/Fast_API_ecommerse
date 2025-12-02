from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.phone_crud import PhoneCRUD
from app.phone.schemas_v1 import PhoneCreate, PhoneUpdate
from app.phone.models import Phone


class PhoneService:
    def __init__(self, crud: PhoneCRUD):
        self.crud = crud

    async def create(
        self,
        session: AsyncSession,
        phone_in: PhoneCreate,
    ) -> Phone:

        if phone_in.price <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Price must be greater than zero")

        return await self.crud.create_phone(
            session=session,
            phone_in=phone_in,)

    async def get_or_404(
        self,
        session: AsyncSession,
        phone_id: int
    ) -> Phone:

        phone = await session.get(Phone, phone_id)
        if not phone:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Phone not found")

        return phone

    async def phone_list(
        self,
        session: AsyncSession
    ) -> list[Phone]:
        return await self.crud.get_phones(session)

    async def update_phone(
        self,
        session: AsyncSession,
        phone_id: int,
        phone_patch: PhoneUpdate
    ) -> Phone:

        phone = await self.get_or_404(session, phone_id)

        updated = await self.crud.patch_phone(
            session=session,
            phone=phone,
            phone_update=phone_patch)

        return updated

    async def delete_phone(
        self,
        session: AsyncSession,
        phone_id: int
    ):

        phone = await self.get_or_404(session, phone_id)

        await self.crud.delete_phone(session, phone)
        return {"detail": "Phone deleted"}


phone_service = PhoneService(PhoneCRUD())

