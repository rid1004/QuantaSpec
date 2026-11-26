import enum
import uuid

from sqlalchemy import Boolean, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from quantaspec.app.db.base import Base, TimeStampMix

class Role(str, enum.Enum):
    GUEST = "guest"
    EDITOR = "editor"
    ADMIN = "admin"

class User(Base, TimeStampMix):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True,default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(120),unique=True,index=True)
    password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean,default=True,server_default='true')
    role: Mapped[Role] = mapped_column(
        Enum(
            Role,
            native_enum=False,
            length=20,
            values_callable = lambda x: [y.value for y in x]
        ),
        default=Role.CUSTOMER,server_default=Role.CUSTOMER.value,
    )