from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db, User, Address
from ..schemas import AddressIn, AddressOut

# Router to handle '/address' routings.
router = APIRouter(prefix = "/address", tags = ["address"])

@router.get("/my", response_model = list[AddressOut])
def get_current_users_address(db: Session = Depends(get_db)):
   """ Get's the current logged in user's address. """
   current_user = db.query(User).get(1)
   if not current_user:
      raise HTTPException(status_code = 404, detail = "No user found!")
   else:
      addresses = current_user.addresses.all()
      return addresses

@router.post("/my/add", response_model = AddressOut)
def add_new_address(address: AddressIn, db: Session = Depends(get_db)):
   """ Adds a new associative address of the user. """
   current_user = db.query(User).get(1)
   if not current_user:
      raise HTTPException(status_code = 404, detail = "No user found!")
   else:
      new_address = Address(line_1 = address.line_1, line_2 = address.line_2, city = address.city, pin_code = address.pin_code)
      current_user.addresses.append(new_address)
      db.commit()
      db.refresh(new_address)
      return new_address
