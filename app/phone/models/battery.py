from app.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.mixins import IdPkMixin


class Battery(Base, IdPkMixin):
    __tablename__ = "battery"

    capacity:Mapped[int]

    fast_charging:Mapped[bool]

    wireless_charging:Mapped[bool]

    charging_connector:Mapped[str]
    
