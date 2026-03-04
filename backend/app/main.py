from fastapi import FastAPI
from uvicorn import Config, Server
from app.modules.auth.phone.route import phone_router
from app.db.session import engine
from sqlalchemy import text
from contextlib import asynccontextmanager
from app.db.base import Base
from app.modules.models import *

# Initializing fastapi
app = FastAPI(title="Rivora")

# db connection check
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Database connected Successfully.")
    except Exception as e:
        print("❌ Database connection failed:", e)
    yield

app = FastAPI(lifespan=lifespan)

# Registering tables into db
Base.metadata.create_all(bind = engine)

# Rivora Routes
app.include_router(phone_router, prefix='/auth')

# Remove this for production -- Only useful for dev
# Only start the server from main.py
if __name__ == "__main__":
    config: Config = Config(  # Just mentioning type -- not needed
        "app.main:app",
        port=5000,
        host="127.0.0.1",
        log_level="info",
        reload=True,
    )
    server: Server = Server(config)
    server.run()
