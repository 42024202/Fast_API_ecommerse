from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.mixins.id_pk_mixin import IdPkMixin


class Color(Base, IdPkMixin):
    __tablename__ = "color"
    name: Mapped[str]

