from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.characters_crud import PhoneScreenCRUD
from app.phone.models import PhoneScreen
from app.phone.schemas_v1.characters.phone_screen import PhoneScreenCreate, PhoneScreenUpdate


class PhoneScreenService:
    def __init__(self, crud: PhoneScreenCRUD):
        self.crud = crud

    async def create(
        self,
        session: AsyncSession,
        screen_in: PhoneScreenCreate,) -> PhoneScreen:

        return await self.crud.create_screen(session, screen_in)

    async def get_or_404(
        self,
        session: AsyncSession,
        screen_id: int) -> PhoneScreen:
        screen = await self.crud.get_screen(session, screen_id)
        if screen is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Phone screen not found")

        return screen

    async def screen_list(
        self,
        session: AsyncSession) -> list[PhoneScreen]:

        return await self.crud.get_screens(session)

    async def update_screen(
        self,
        session: AsyncSession,
        screen_id: int,
        screen_in: PhoneScreenUpdate) -> PhoneScreen:

        screen = await self.get_or_404(session, screen_id)
        updated = await self.crud.update_screen(session, screen, screen_in)

        return updated

    async def delete_screen(
        self,
        session: AsyncSession,
        screen_id: int):

        screen = await self.get_or_404(session, screen_id)
        await self.crud.delete_screen(session, screen)
        return {"detail": "Phone screen deleted"}


phone_screen_service = PhoneScreenService(PhoneScreenCRUD())

