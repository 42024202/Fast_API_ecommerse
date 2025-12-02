from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.phone.models import Phone
from app.phone.schemas_v1 import PhoneCreate, PhoneUpdate


class PhoneCRUD:
    async def create_phone(
            self,
            phone_in: PhoneCreate,
            session: AsyncSession
            ) -> Phone:
        phone = Phone(**phone_in.model_dump())
        session.add(phone)
        await session.commit()
        await session.refresh(phone)
        return phone

    async def get_phone(
            self,
            session: AsyncSession,
            id: int
            ) -> Phone | None:
        return await session.get(Phone, id)
    

    async def get_phones(
            self,
            session: AsyncSession
            ) -> list[Phone]:
        stmnt = select(Phone).order_by(Phone.id)
        result:Result = await session.execute(stmnt)
        products = result.scalars().all()

        return list(products)


    async def patch_phone(
            self,
            session: AsyncSession,
            phone: Phone,
            phone_update: PhoneUpdate
            ):
        update_data = phone_update.model_dump(exclude_unset=True)

        for name, value in update_data.items():
            setattr(phone, name, value)

        await session.commit()
        await session.refresh(phone)

        return phone


    async def delete_phone(
            self,
            session: AsyncSession,
            phone: Phone
            ):
        await session.delete(phone)
        await session.commit()

