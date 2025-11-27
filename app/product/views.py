from sqlalchemy.ext.asyncio import AsyncSession
from .crud import (create_product, get_product_by_id, get_products,
                   patch_product, delete_product
)
from .schemas.schema_v1 import ProductCreate, ProductUpdate
from .models import Product


class ProductServiceV1:
    """Business logic for products."""

    async def list_products(self, session: AsyncSession):
        return await get_products(session)

    async def get_product(self, session: AsyncSession, id: int):
        return await get_product_by_id(session, id)

    async def create_product(self, session: AsyncSession, product_in: ProductCreate):
        return await create_product(product_in, session)

    async def update_product_part(self, session: AsyncSession, product: Product, product_update: ProductUpdate):
        return await patch_product(session=session, product=product, product_update=product_update)

    async def remove_product(self, session: AsyncSession, product: Product):
        return await delete_product(session, product)

