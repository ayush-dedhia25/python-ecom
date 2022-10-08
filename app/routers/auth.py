from pydantic import BaseModel, EmailStr, Field
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..database.models import User
from ..schemas import SessionUser
from ..utils import jwt, hashing

class AuthIn(BaseModel):
   email: EmailStr = Field(...)
   password: str = Field(...)

router = APIRouter(prefix = "/auth", tags = ["authentication"])

@router.post("/login")
def login_user(usr: AuthIn, db: Session = Depends(get_db)):
   user = db.query(User).filter_by(email = usr.email).first()
   if not user:
      raise HTTPException(status_code = 404, detail = "User not found!")
   else:
      salt, password = user.enc, user.password
      if hashing.cmp_str(salt, password, usr.password):
         session_user = SessionUser(ID = user.ID, name = user.name, email = user.email)
         access_token = jwt.create_access_token(session_user.dict())
         return { "access_token": access_token }
      else:
         raise HTTPException(status_code = 403, detail = "Invalid credentials!")
