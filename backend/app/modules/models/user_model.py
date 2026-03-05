from sqlalchemy import String, Boolean, UUID
from datetime import datetime, timezone
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

class User( Base ):
    """Table that contains information about the user."""
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(  UUID(as_uuid=True), default=uuid.uuid4, primary_key=True )
    username: Mapped[str] = mapped_column( String, unique=True, index=True )
    fullname: Mapped[str] = mapped_column( String )
    email: Mapped[str | None] = mapped_column( String, nullable=True, unique=True ) # Optional
    email_verified: Mapped[bool] = mapped_column( Boolean, default=False )
    phone_number: Mapped[str | None] = mapped_column( String, nullable=True, unique=True ) # Optional
    phone_verified: Mapped[bool] = mapped_column( Boolean, default=False )
    created_at: Mapped[datetime] = mapped_column( default=lambda: datetime.now(timezone.utc) )
    updated_at: Mapped[datetime] = mapped_column( default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc) )

    # Relation
    identities = relationship("Identity", back_populates="user", cascade="all, delete-orphan") # deletes record in both the table
