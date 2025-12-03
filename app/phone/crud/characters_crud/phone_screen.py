from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.phone.models import PhoneScreen
from app.phone.schemas_v1.characters.phone_screen import PhoneScreenCreate, PhoneScreenUpdate


class PhoneScreenCRUD:

    async def create_screen(
            self,
            session: AsyncSession,
            screen_in: PhoneScreenCreate) -> PhoneScreen:

        screen = PhoneScreen(**screen_in.model_dump())
        session.add(screen)
        await session.commit()
        await session.refresh(screen)
        return screen

    async def get_screen(
            self,
            session: AsyncSession,
            screen_id: int) -> PhoneScreen | None:

        return await session.get(PhoneScreen, screen_id)

    async def get_screens(
            self,
            session: AsyncSession) -> list[PhoneScreen]:

        stmt = select(PhoneScreen).order_by(PhoneScreen.id)
        result: Result = await session.execute(stmt)
        screens = result.scalars().all()
        return list(screens)

    async def update_screen(
            self,
            session: AsyncSession,
            screen: PhoneScreen, screen_in: PhoneScreenUpdate) -> PhoneScreen:
        update_data = screen_in.model_dump(exclude_unset=True)
        for name, value in update_data.items():
            setattr(screen, name, value)

        await session.commit()
        await session.refresh(screen)
        return screen

    async def delete_screen(
            self,
            session: AsyncSession,
            screen: PhoneScreen):

        await session.delete(screen)
        await session.commit()

