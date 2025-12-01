from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.mixins import IdPkMixin, TimestampMixin, OwnerMixin


class Brand(Base):
    __tablename__ = "brand"
    name: Mapped[str] = mapped_column(
            unique=True,
            nullable=False
            )
