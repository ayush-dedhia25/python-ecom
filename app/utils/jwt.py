from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from ..schemas import SessionUser

SECRET_KEY = "b927220cc398dc7b756eb7e0b0faaad3dcfce3797b059cc53fb08fb2489844e3"
EXP_TIME = 30
ALGORITHM = "HS256"

OAuth2_Scheme = OAuth2PasswordBearer(tokenUrl = "http://localhost:8000/auth/login")

def create_access_token(data: dict) -> str:
   to_encode = data.copy()
   expire = datetime.utcnow() + timedelta(minutes = EXP_TIME)
   to_encode.update({ "exp": expire })
   encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
   return encoded_jwt

def get_current_user(token: str = Depends(OAuth2_Scheme)) -> SessionUser:
   exception = HTTPException(
      status_code = 401,
      detail = "Couldn't validite credentials",
      headers = { "WWW-Authenticate": "Bearer" }
   )
   try:
      payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
      name: str = payload.get("name")
      if name is None:
         raise exception
      else:
         return SessionUser(ID = payload.get("ID"), name = name, email = payload.get("email"))
   except JWTError:
      raise exception