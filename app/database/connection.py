from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database file scheme + location
DB_FILE = "sqlite:///./app.sqlite3"
# Create sqlite3 connection engine
engine = create_engine(DB_FILE, connect_args = { "check_same_thread": False }, echo = True)
# Create local connection manager
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False)
# Create a base model for the user defined models to derive from.
Base = declarative_base()

# Gets the local connection manager
def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()