from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

# Define your schemas here...
class Response(BaseModel):
   ID: int
   created_at: datetime
   modified_at: datetime
   
   class Config:
      orm_mode = True

class AddressIn(BaseModel):
   line_1: str = Field(...)
   line_2: str = Field(...)
   city: str = Field(...)
   pin_code: str = Field(..., min_length = 6, max_length = 8)

class AddressUp(BaseModel):
   line_1: str | None = Field(None, min_length = 5)
   line_2: str | None = Field(None, min_length = 5)
   city: str | None = Field(None, min_length = 5)
   pin_code: str | None = Field(None, min_length = 6, max_length = 8)

class AddressOut(Response):
   line_1: str
   line_2: str
   city: str
   pin_code: str

class UserIn(BaseModel):
   name: str = Field(..., min_length = 2)
   email: EmailStr
   password: str = Field(..., min_length = 6)

class UserNameUp(BaseModel):
   name: str = Field(..., min_length = 2)

class UserEmailUp(BaseModel):
   email: EmailStr = Field(...)

class UserPasswordUp(BaseModel):
   password: str = Field(..., min_length = 6)

class UserOut(Response):
   name: str
   email: str
   is_verified: bool

class SessionUser(BaseModel):
   ID: int
   name: str
   email: EmailStr
