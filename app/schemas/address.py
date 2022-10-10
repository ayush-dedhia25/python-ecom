from datetime import datetime
from pydantic import BaseModel, Field

class AddressIn(BaseModel):
   line_1: str = Field(..., min_length = 10)
   line_2: str = Field(..., min_length = 5)
   city: str = Field(..., min_length = 4)
   pin_code: str = Field(..., min_length = 6, max_length = 8)

class AddressOut(BaseModel):
   ID: int
   line_1: str
   line_2: str
   city: str
   pin_code: str
   created_at: datetime
   modified_at: datetime
   
   class Config:
      orm_mode = True

class AddressUp(BaseModel):
   line_1: str | None = Field(None, min_length = 10)
   line_2: str | None = Field(None, min_length = 5)
   city: str | None = Field(None, min_length = 4)
   pin_code: str | None = Field(None, min_length = 6, max_length = 8)