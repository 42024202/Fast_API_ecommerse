from app.core import Base
from sqlalchemy.orm import Mapped
from app.mixins.id_pk_mixin import IdPkMixin


class Product(IdPkMixin, Base):
    __tablename__ = "product"
    name:Mapped[str]
    price:Mapped[int]
    description:Mapped[str]
