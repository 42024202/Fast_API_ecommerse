from fastapi import Depends, HTTPException
from app.user.models.user import UserRole
from app.user.services import fastapi_users


def admin_only(user=Depends(fastapi_users.current_user())):
    if user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Admins only")
    return user

