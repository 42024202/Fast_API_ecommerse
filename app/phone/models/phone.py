from app.core import Base
from enum import Enum as PyEnum
from sqlalchemy import ForeignKey, Boolean, Integer, String, Text, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.mixins import IdPkMixin, TimestampMixin, OwnerMixin


class Condition(PyEnum):
    NEW = "new"
    USED = "used"
    BROKEN = "broken"


class Phone(Base, IdPkMixin, TimestampMixin, OwnerMixin):
    __tablename__ = "phone"

    price:Mapped[int] = mapped_column(
            Integer,
            nullable=False
            )

    brand_id:Mapped[int] = mapped_column(
            ForeignKey("brand.id", ondelete="CASCADE"),
            nullable=False
            )

    model_id:Mapped[int] = mapped_column(
            ForeignKey("phone_model.id", ondelete="CASCADE"),
            nullable=False
            )

    storage:Mapped[int]=mapped_column(
            ForeignKey("storage.id", ondelete="CASCADE"),
            nullable=False
            )

    color_id:Mapped[int] = mapped_column(
            ForeignKey("color.id", ondelete="CASCADE"),
            nullable=False
            )

    condition:Mapped[Condition] = mapped_column(
            SqlEnum(Condition, name="phone_condition"),
            nullable=False
            )

    is_active:Mapped[bool]

    description:Mapped[str] = mapped_column(Text, nullable=False)


    images = relationship("PhoneImage", back_populates="phone", cascade="all, delete-orphan")
    brand = relationship("Brand")
    model = relationship("PhoneModel")
    storage = relationship("Storage")
    color = relationship("Color")

