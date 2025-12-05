from app.core import Base
from enum import Enum as PyEnum
from sqlalchemy import ForeignKey, Integer, Text, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.mixins import IdPkMixin, TimestampMixin


class Condition(str, PyEnum):
    NEW = "new"
    USED = "used"
    BROKEN = "broken"


class Phone(Base, IdPkMixin, TimestampMixin):
    __tablename__ = "phone"

    price: Mapped[int] = mapped_column(
        Integer,
        nullable=False
        )

    brand_id: Mapped[int] = mapped_column(
        ForeignKey("brand.id"),
        nullable=False
        )

    model_id: Mapped[int] = mapped_column(
        ForeignKey("phone_model.id"),
        nullable=False
        )

    battery_id: Mapped[int] = mapped_column(
        ForeignKey("battery.id"),
        nullable=False
        )

    screen_id: Mapped[int] = mapped_column(
        ForeignKey("phone_screen.id"),
        nullable=False
        )

    oc_version: Mapped[str]
    cpu: Mapped[str]
    cpu_cores: Mapped[int]
    cpu_frequency: Mapped[int]
    gpu: Mapped[str]
    ram: Mapped[int]

    storage_id: Mapped[int] = mapped_column(
        ForeignKey("storage.id"),
        nullable=False
        )

    condition: Mapped[Condition] = mapped_column(
        SqlEnum(Condition, name="phone_condition"),
        nullable=False
        )

    release_year: Mapped[int]
    is_active: Mapped[bool]

    description: Mapped[str] = mapped_column(Text, nullable=False)

    country_of_origin_id: Mapped[int] = mapped_column(
        ForeignKey("country_of_origin.id"),
        nullable=False
        )


    #Relationship
    images = relationship(
        "PhoneImage",
        back_populates="phone",
        cascade="all, delete-orphan"
        )

    brand = relationship(
        "Brand",
        back_populates="phones"    
        )

    model = relationship(
        "Model",
        back_populates="phones"
        )

    battery = relationship(
            "Battery",
            back_populates="phones"
            )

    storage = relationship(
            "Storage",
            back_populates="phones"
            )

    screen = relationship(
            "PhoneScreen",
            back_populates="phones"
            )

    country_of_origin = relationship(
        "CountryOfOrigin",
        back_populates="phones"
        )

    stocks = relationship(
        "Stock",
        back_populates="phone",
        cascade="all, delete-orphan")

