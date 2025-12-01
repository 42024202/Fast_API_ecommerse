from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core import Base
from app.mixins import IdPkMixin, TimestampMixin


class PhoneImage(Base, IdPkMixin, TimestampMixin):
    __tablename__ = "phone_image"

    url: Mapped[str] = mapped_column(
            String,
            nullable=False
            )

    phone_id: Mapped[int] = mapped_column(
        ForeignKey("phone.id", ondelete="CASCADE"),
        nullable=False
        )

    phone = relationship("Phone", back_populates="images")

