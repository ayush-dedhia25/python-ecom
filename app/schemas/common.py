from pydantic import BaseModel, EmailStr

# Define your schemas here...
class SessionUser(BaseModel):
   ID: int
   name: str
   email: EmailStr

class UpdateInfo(BaseModel):
   status_code: int
   detail: str