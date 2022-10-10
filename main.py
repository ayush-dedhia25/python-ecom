from fastapi import FastAPI
from app.database.connection import engine
from app.database.models import Base
from app.routers import acc_router, addr_router, auth_router, cc_router

# Main server instance
app = FastAPI()

# Sqlite database migrations
Base.metadata.create_all(bind = engine)

app.include_router(auth_router)
app.include_router(acc_router)
app.include_router(addr_router)
app.include_router(cc_router)