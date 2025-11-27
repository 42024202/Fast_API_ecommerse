from fastapi import APIRouter
from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.product.models.product import Product
from app.product.services import ProductServiceV1
from app.core.db_helpers import db_helper
from app.product.schemas.schema_v1 import ProductCreate, ProductOut, ProductUpdate
from app.product.dependencies import get_product_or_404


router = APIRouter(prefix="/products", tags=["Product"])

product_service = ProductServiceV1()


@router.get("/", response_model=list[ProductOut])
async def get_products(session: AsyncSession = Depends(db_helper.scoped_session_dependancy)):
    """GET all products"""
    return await product_service.list_products(session)


@router.get("/{id}/", response_model=ProductOut)
async def get_product(product:Product = Depends(get_product_or_404),):
    return product


@router.post("/create/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy)
):
    """CREATE product"""
    return await product_service.create_product(session, product_in)


@router.patch("/update/{id}/")
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(get_product_or_404),
        session: AsyncSession = Depends(db_helper.scoped_session_dependancy),
        ):
    return await product_service.update_product_part(session=session, product=product, product_update=product_update)


@router.delete("/delete/{id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
        product: Product = Depends(get_product_or_404),
        session: AsyncSession = Depends(db_helper.scoped_session_dependancy),
        ) -> None:
    await product_service.remove_product(session, product)
