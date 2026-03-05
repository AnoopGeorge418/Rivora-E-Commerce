from sqlalchemy import String, Boolean, UUID
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class MagicLink(Base):
    """Table that contains magic link login information."""
    __tablename__ = "magic_links"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    email: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    token_hash: Mapped[str] = mapped_column(
        String(255)
    )

    expires_at: Mapped[datetime]

    is_used: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    