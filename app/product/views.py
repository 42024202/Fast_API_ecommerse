from fastapi import APIRouter, Depends, HTTPException, status, Depends
from ..core.db_helpers import db_helper
from .crud import create_product, get_product_by_id, get_products
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas.schema_v1 import ProductCreate, ProductOut


router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/", response_model=list[ProductOut])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependancy)):
    return await get_products(session)


@router.get("/{id}/", response_model=ProductOut)
async def get_item(id: int, session: AsyncSession = Depends(db_helper.session_dependancy)):
    product = await get_product_by_id(session=session, id=id)
    if product:
        return product
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {id} not found"
                )


@router.post("/", response_model=ProductOut)
async def create_product(
        product_in:ProductCreate,
        session: AsyncSession = Depends(db_helper.session_dependancy)
        ):
    return await create_product(session=session, product_in=product_in)
