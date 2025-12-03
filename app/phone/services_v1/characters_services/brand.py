from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.phone.crud.characters_crud import BrandCRUD
from app.phone.models import Brand
from app.phone.schemas_v1.characters import BrandUpdate, BrandCreate


class BrandService:
    def __init__(self, crud: BrandCRUD):
        self.crud = crud

    async def create(
        self,
        session: AsyncSession,
        brand_in: BrandCreate,
        ) -> Brand:

        return await self.crud.create_brand(session, brand_in)

    async def get_or_404(
        self,
        session: AsyncSession,
        brand_id: int
        ) -> Brand:

        brand = await self.crud.get_brand(session, brand_id)
        if brand is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Brand not found"
            )
        return brand

    async def brand_list(
            self,
            session: AsyncSession
            ) -> list[Brand]:

        return await self.crud.get_brands(session)

    async def update_brand(
            self,
            session: AsyncSession,
            brand_id: int,
            brand_in: BrandUpdate
            ) -> Brand:

        brand = await self.get_or_404(session, brand_id)
        updated = await self.crud.update_brand(session, brand, brand_in)
        
        return updated

    async def delete_brand(
            self,
            session: AsyncSession,
            brand_id: int
            ):
        brand = await self.get_or_404(session, brand_id)
        await self.crud.delete_brand(session, brand)
        return {"detail": "Brand deleted"}


brand_service = BrandService(BrandCRUD())

