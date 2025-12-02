from app.phone.services_v1.phone import phone_service
from app.core.db_helpers import db_helper
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db_helpers import db_helper
from app.phone.schemas_v1 import PhoneCreate, PhoneOut, PhoneUpdate
from app.phone.dependencies import get_phone_or_404


router = APIRouter(prefix="/phone", tags=["phone"])


@router.get("/", response_model=list[PhoneOut])
async def list_phones(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy)):

    """Get all phones"""
    return await phone_service.phone_list(session)


@router.get("/{phone_id}/", response_model=PhoneOut)
async def get_phone(
    phone=Depends(get_phone_or_404),):

    """Get one phone by ID"""
    return phone


@router.post("/",
    response_model=PhoneOut,
    status_code=status.HTTP_201_CREATED)

async def create_phone(
    phone_in: PhoneCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),):
    """Create a new phone"""
    return await phone_service.create(session, phone_in)


@router.patch("/{phone_id}/",
    response_model=PhoneOut)

async def update_phone(
    phone_update: PhoneUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),
    phone=Depends(get_phone_or_404),):

    """Update phone partially"""
    return await phone_service.update_phone(
        session=session,
        phone_id=phone.id,
        phone_patch=phone_update)


@router.delete(
    "/{phone_id}/",
    status_code=status.HTTP_204_NO_CONTENT)

async def delete_phone(
    session: AsyncSession = Depends(db_helper.scoped_session_dependancy),
    phone=Depends(get_phone_or_404)):

    """Delete phone"""
    await phone_service.delete_phone(session, phone.id)
    return None

