from fastapi import APIRouter

from product.views import router as product_router


router = APIRouter()
router.include_router(router=product_router, prefix="/product")

