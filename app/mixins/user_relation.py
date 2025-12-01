from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped


class OwnerMixin:
    owner_idm: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner = relationship("User", lazy="joined")

