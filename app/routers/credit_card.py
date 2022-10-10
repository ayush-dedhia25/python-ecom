from pydantic import BaseModel, EmailStr, Field
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db, User, CreditCard
from ..schemas import SessionUser, CardIn, CardOut
from ..utils import get_current_user

router = APIRouter(tags = ["Payment", "Credit Cards"])

@router.post("/account/payment/card/add", response_model = CardOut)
def add_payment_card(
   card: CardIn,
   curr_usr: SessionUser = Depends(get_current_user),
   db: Session = Depends(get_db)
):
   """ Adds a new payment card. """
   user = db.query(User).get(curr_usr.ID)
   if not user:
      raise HTTPException(status_code = 404, detail = "Account missing!")
   else:
      new_card = CreditCard(card_type = card.card_type, number = card.number, holderID = curr_usr.ID)
      try:
         db.add(new_card)
         db.flush()
      except LookupError as e:
         db.rollback()
         raise HTTPException(status_code = 500, detail = "Seems! like your card isn't of a valid type!")
      else:
         db.commit()
         db.refresh(new_card)
         return new_card
