from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database.connection import get_db
from ..database.models import User
from ..schemas import UserIn, UserOut, UserEmailUp, UserNameUp, SessionUser
from ..utils.jwt import get_current_user 

router = APIRouter(prefix = "/account", tags = ["account"])

@router.post("/create", response_model = UserOut)
async def create_account(user: UserIn, db: Session = Depends(get_db)):
   """ Creates a new account/user for the site. """
   salt, hashed = hashing.hash_str(user.password)
   new_user = User(name = user.name, email = user.email, password = hashed, enc = salt)
   try:
      db.add(new_user)
      db.flush()
   except IntegrityError:
      db.rollback()
      raise HTTPException(status_code = 409, detail = "Email is already taken!")
   else:
      db.commit()
      db.refresh(new_user)
      return new_user

@router.get("/me", response_model = UserOut)
def get_account(curr_user: SessionUser = Depends(get_current_user), db: Session = Depends(get_db)):
   """ Gets the current logged-in user and returns it. """
   user = db.query(User).get(curr_user.ID)
   if not user:
      raise HTTPException(status_code = 404, detail = "Account missing!")
   else:
      return user

@router.put("/me/update/email")
def update_email(
   acc: UserEmailUp,
   curr_user: SessionUser = Depends(get_current_user),
   db: Session = Depends(get_db)
):
   """ Updates a user's email address. """
   user = db.query(User).get(curr_user.ID)
   if not user:
      raise HTTPException(status_code = 404, detail = "Account missing!")
   elif acc.email == curr_user.email:
      raise HTTPException(status_code = 400, detail = "Seems like you have provided the old email address!")
   else:
      email_in_use = db.query(User).filter_by(email = acc.email).first()
      if email_in_use:
         raise HTTPException(status_code = 409, detail = "Email is already taken!")
      else:
         # Update the email property
         setattr(user, "email", acc.email)
         db.commit()
         return { "status_code": 200, "detail": "Email updated!" }

@router.put("/me/update/name")
def update_name(
   acc: UserNameUp,
   curr_user: SessionUser = Depends(get_current_user),
   db: Session = Depends(get_db)
):
   """ Updates a user's name. """
   user = db.query(User).get(curr_user.ID)
   if not user:
      raise HTTPException(status_code = 404, detail = "Account missing!")
   else:
      # Update the name property
      setattr(user, "name", acc.name)
      db.commit()
      return { "status_code": 200, "detail": "Name updated!" }
