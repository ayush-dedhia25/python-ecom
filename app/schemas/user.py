from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

class UserIn(BaseModel):
   name: str = Field(..., min_length = 2)
   email: EmailStr
   password: str = Field(..., min_length = 6)

class UserOut(BaseModel):
   ID: int
   name: str
   email: str
   is_verified: bool
   created_at: datetime
   modified_at: datetime
   
   class Config:
      orm_mode = True

class UserNameUp(BaseModel):
   name: str = Field(..., min_length = 2)

class UserEmailUp(BaseModel):
   email: EmailStr = Field(...)

class UserPasswordUp(BaseModel):
   password: str = Field(..., min_length = 6)