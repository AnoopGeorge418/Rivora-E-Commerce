from sqlalchemy import String, Boolean, UUID, ForeignKey, Enum, UniqueConstraint
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid
from app.modules.schemas.auth_providers_schema import AuthProviders

class Identity( Base ):
    """Table that contains information about login/register provider"""
    __tablename__ = "identities"

    id: Mapped[uuid.UUID] = mapped_column(  UUID(as_uuid=True), default=uuid.uuid4, primary_key=True )
    user_id: Mapped[uuid.UUID] = mapped_column( UUID(as_uuid=True), ForeignKey("users.id") )
    provider: Mapped[AuthProviders] = mapped_column( Enum(AuthProviders, name="auth_providers_enum"), nullable=False )
    provider_id: Mapped[str] = mapped_column(String)
    provider_email: Mapped[str] = mapped_column(String)
    provider_email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column( default=lambda: datetime.now(timezone.utc) )

    __table_args__ = (
        UniqueConstraint("provider", "provider_id"), # make sure that only one user can have same id.
    )

    # Relation
    user = relationship("User", back_populates="identities") # relates to users table
