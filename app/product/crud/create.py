from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.product import Product
from ..schemas.schema_v1 import ProductCreate


async def create_product(product_in:ProductCreate, session:AsyncSession) -> Product:
    """Create product"""
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product
    
