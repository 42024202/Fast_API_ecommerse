from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_

from app.phone.crud.phone_crud import PhoneCRUD
from app.phone.schemas_v1.phone import PhoneCreate, PhoneUpdate
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


    async def filter_phones(self, session: AsyncSession, filters):
        query = select(Phone)
        conditions = []
        
        """brand"""
        if filters.brand_id:
            conditions.append(Phone.brand_id == filters.brand_id)

        """model"""
        if filters.model_id:
            conditions.append(Phone.model_id == filters.model_id)

        """price range"""
        if filters.price_from:
            conditions.append(Phone.price >= filters.price_from)

        if filters.price_to:
            conditions.append(Phone.price <= filters.price_to)

        """ram"""
        if filters.ram_from:
            conditions.append(Phone.ram >= filters.ram_from)

        if filters.ram_to:
            conditions.append(Phone.ram <= filters.ram_to)

        """storage"""
        if filters.storage_id:
            conditions.append(Phone.storage_id == filters.storage_id)

        """condition"""
        if filters.condition:
            conditions.append(Phone.condition == filters.condition)

        """year range"""
        if filters.release_year_from:
            conditions.append(Phone.release_year >= filters.release_year_from)

        if filters.release_year_to:
            conditions.append(Phone.release_year <= filters.release_year_to)

        """full text search"""
        if filters.search:
            conditions.append(
                or_(
                    Phone.cpu.ilike(f"%{filters.search}%"),
                    Phone.gpu.ilike(f"%{filters.search}%"),
                    Phone.description.ilike(f"%{filters.search}%"),
                )
            )

        if conditions:
            query = query.where(and_(*conditions))

        result = await session.execute(query)
        return result.scalars().all()


phone_service = PhoneService(PhoneCRUD())

