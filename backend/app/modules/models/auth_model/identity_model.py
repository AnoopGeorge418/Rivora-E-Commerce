from sqlalchemy import String, Boolean, UUID, ForeignKey, Enum, UniqueConstraint
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from app.modules.schemas.auth_providers_schema import AuthProviders


class Identity(Base):
    """Table that contains information about login/register providers."""
    __tablename__ = "identities"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        index=True
    )

    provider: Mapped[AuthProviders] = mapped_column(
        Enum(AuthProviders, name="auth_providers_enum"),
        nullable=False
    )

    provider_id: Mapped[str] = mapped_column(
        String(255)
    )

    provider_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    provider_email_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        UniqueConstraint("provider", "provider_id"),
    )

    # Relationships
    user = relationship(
        "User",
        back_populates="identities"
    )
    