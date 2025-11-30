from typing import TYPE_CHECKING
from app.core import Base
from app.mixins.id_pk_mixin import IdPkMixin
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, mapped_column


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(IdPkMixin, SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'user'
    
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
    
