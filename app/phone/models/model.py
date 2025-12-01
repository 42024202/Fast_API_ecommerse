from app.core import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.mixins.id_pk_mixin import IdPkMixin


class Model(IdPkMixin, Base):
    __tablename__ = "phone_model"
    name: Mapped[str]
    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id"))

