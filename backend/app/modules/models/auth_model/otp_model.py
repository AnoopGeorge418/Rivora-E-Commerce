from sqlalchemy import String, Boolean, UUID, Integer
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class OTP(Base):
    """Table that contains OTP information."""
    __tablename__ = "otps"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    provider_id: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    otp_hash: Mapped[str] = mapped_column(
        String(255)
    )

    attempts: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    max_attempts: Mapped[int] = mapped_column(
        Integer,
        default=5
    )

    is_used: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    expires_at: Mapped[datetime]

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    