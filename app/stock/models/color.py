from app.core import Base
from app.mixins import IdPkMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class Color(IdPkMixin, Base):
    __tablename__ = "color"

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False)

    stocks = relationship(
        "Stock",
        back_populates="color",
        cascade="all, delete-orphan")

