from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

from app.phone.models import Brand
from app.phone.schemas_v1.characters.brand import BrandCreate, BrandUpdate


class BrandCRUD:

    async def create_brand(
            self,
            session: AsyncSession,
            brand_in: BrandCreate
            ) -> Brand:

        brand = Brand(**brand_in.model_dump())
        session.add(brand)
        await session.commit()
        await session.refresh(brand)
        return brand

    async def get_brand(
                self,
                session: AsyncSession,
                brand_id: int
            ) -> Brand | None:

        return await session.get(Brand, brand_id)

    async def get_brands(
                self,
                session: AsyncSession
            ) -> list[Brand]:
        stmt = select(Brand).order_by(Brand.id)
        result: Result = await session.execute(stmt)
        brands = result.scalars().all()
        return list(brands)

    async def update_brand(
                self,
                session: AsyncSession,
                brand: Brand,
                brand_in: BrandUpdate
            ) -> Brand:

        update_data = brand_in.model_dump(exclude_unset=True)

        for name, value in update_data.items():
            setattr(brand, name, value)

        await session.commit()
        await session.refresh(brand)
        return brand


    async def delete_brand(
                self,
                session: AsyncSession,
                brand: Brand
            ):
        await session.delete(brand)
        await session.commit()

