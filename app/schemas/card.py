from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum

# Define your schemas here...
class CardIn(BaseModel):
   card_type: str = Field(...)
   number: str = Field(..., min_length = 19, max_length = 19)

class CardOut(BaseModel):
   ID: int
   card_type: str
   number: str
   created_at: datetime
   modified_at: datetime
   
   class Config:
      orm_mode = True

class CardTypes(str, Enum):
   VISA = "VISA"
   STANDARD_CHARTERED_CREDIT_CARD = "STANDARD_CHARTERED_CREDIT_CARD"
   BUSINESS = "BUSINESS"
   DISCOVER_FINANCIAL_SERVICES = "DISCOVER_FINANCIAL_SERVICES"
   CITIBANK_CREDIT_CARD = "CITIBANK_CREDIT_CARD"
   LIC_CREDIT_CARD = "LIC_CREDIT_CARD"
   UNION_BANK_CREDIT_CARD = "UNION_BANK_CREDIT_CARD"
   CHARGE_CARD = "CHARGE_CARD"
   RBL_CARD = "RBL_CARD"
   CORPORATE_CREDIT_CARD = "CORPORATE_CREDIT_CARD"
   LIFESTYLE_CARD = "LIFESTYLE_CARD"
   ENTERTAINMENT = "ENTERTAINMENT"
