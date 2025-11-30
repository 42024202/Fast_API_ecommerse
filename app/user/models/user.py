import enum

from typing import TYPE_CHECKING
from app.core import Base
from app.mixins.id_pk_mixin import IdPkMixin
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from sqlalchemy import Enum as PgEnum
from sqlalchemy.orm import Mapped, mapped_column


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class UserRole(str, enum.Enum):
    USER = "USER",
    ADMIN = "ADMIN"


class User(IdPkMixin, SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'user'
    
    role:Mapped[UserRole] = mapped_column(
            PgEnum(UserRole, name="userrole"),
            default=UserRole.USER,
            nullable=False
            )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
    
