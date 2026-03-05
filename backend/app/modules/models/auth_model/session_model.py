from sqlalchemy import String, Boolean, UUID, ForeignKey
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class Session(Base):
    """Table contains refresh token sessions."""
    __tablename__ = "sessions"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        index=True
    )

    token_hash: Mapped[str] = mapped_column(
        String(255)
    )

    device_id: Mapped[str] = mapped_column(
        String(255)
    )

    ip_address: Mapped[str] = mapped_column(
        String(50)
    )

    user_agent: Mapped[str] = mapped_column(
        String(500)
    )

    revoked: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    expires_at: Mapped[datetime]

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )

    last_used_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )
