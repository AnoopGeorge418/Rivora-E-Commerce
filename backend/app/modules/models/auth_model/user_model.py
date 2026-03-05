from sqlalchemy import String, Boolean, UUID
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid


class User(Base):
    """Table that contains information about the user."""
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True
    )

    fullname: Mapped[str] = mapped_column(
        String(120)
    )

    email: Mapped[str | None] = mapped_column(
        String(255), nullable=True, unique=True
    )

    email_verified: Mapped[bool] = mapped_column(
        Boolean, default=False
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(20), nullable=True, unique=True
    )

    phone_verified: Mapped[bool] = mapped_column(
        Boolean, default=False
    )

    password_hash: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationships
    identities = relationship(
        "Identity",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    