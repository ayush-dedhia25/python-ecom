from fastapi import FastAPI
from app.database.connection import engine
from app.database.models import Base
from app.routers import account, address, auth

# Main server instance
app = FastAPI()

# Sqlite database migrations
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(account.router)
app.include_router(address.router)