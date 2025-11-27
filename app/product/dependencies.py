from fastapi import Depends, HTTPException, status, Path
from app.core.db_helpers import db_helper
from app.product.views import ProductServiceV1
from app.product.models import Product
from typing import Annotated

product_service = ProductServiceV1()

async def get_product_or_404(
    product_id: Annotated[int, Path],
    session = Depends(db_helper.scoped_session_dependancy),
) -> Product:
    product = await product_service.get_product(session, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {id} not found"
        )
    return product

