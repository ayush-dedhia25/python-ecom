from pydantic import BaseModel, EmailStr, Field
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db, User
from ..schemas import SessionUser
from ..utils import cmp_str, create_access_token

class AuthIn(BaseModel):
   email: EmailStr = Field(...)
   password: str = Field(..., min_length = 6)

router = APIRouter(prefix = "/auth", tags = ["authentication"])

@router.post("/login")
def login_user(usr: AuthIn, db: Session = Depends(get_db)):
   user = db.query(User).filter_by(email = usr.email).first()
   if not user:
      raise HTTPException(status_code = 404, detail = "User not found!")
   else:
      salt, password = user.enc, user.password
      if cmp_str(salt, password, usr.password):
         session_user = SessionUser(ID = user.ID, name = user.name, email = user.email)
         access_token = create_access_token(session_user.dict())
         return { "access_token": access_token }
      else:
         raise HTTPException(status_code = 403, detail = "Invalid credentials!")
