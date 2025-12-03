from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.characters_crud import BatteryCRUD
from app.phone.models import Battery
from app.phone.schemas_v1.characters.battery import BatteryCreate, BatteryUpdate


class BatteryService:
    def __init__(self, crud: BatteryCRUD):
        self.crud = crud

    async def create(
        self,
        session: AsyncSession,
        battery_in: BatteryCreate,) -> Battery:

        return await self.crud.create_battery(session, battery_in)

    async def get_or_404(
        self,
        session: AsyncSession,
        battery_id: int) -> Battery:

        battery = await self.crud.get_battery(session, battery_id)
        if battery is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Battery not found")

        return battery

    async def battery_list(
        self,
        session: AsyncSession) -> list[Battery]:

        return await self.crud.get_batteries(session)

    async def update_battery(
        self,
        session: AsyncSession,
        battery_id: int,
        battery_in: BatteryUpdate) -> Battery:
        battery = await self.get_or_404(session, battery_id)
        updated = await self.crud.update_battery(session, battery, battery_in)

        return updated

    async def delete_battery(
        self,
        session: AsyncSession,
        battery_id: int):

        battery = await self.get_or_404(session, battery_id)
        await self.crud.delete_battery(session, battery)
        return {"detail": "Battery deleted"}


battery_service = BatteryService(BatteryCRUD())

