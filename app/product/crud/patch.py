from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.product import Product
from ..schemas.schema_v1 import ProductUpdate


async def patch_product(session:AsyncSession, product:Product, product_update:ProductUpdate):
    """Create product"""
    for name, value in product_update.model_dump(exclude_unset=True).items():
       setattr(product, name, value)
       await session.commit()
       return product

