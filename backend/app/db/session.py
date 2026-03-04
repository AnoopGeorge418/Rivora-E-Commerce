from sqlalchemy import create_engine
from app.core.config import app_settings
from sqlalchemy.orm import sessionmaker

# Creating database engine
engine = create_engine(app_settings.DATABASE_URL)

# Creating session
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)
    
