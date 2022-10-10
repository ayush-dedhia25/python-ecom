from datetime import datetime
from sqlalchemy import Column, ForeignKey, Enum
from sqlalchemy.types import String, Integer, Boolean, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from .connection import Base
from ..schemas import CardTypes

# Define your models here...
class Abstract:
   ID = Column(Integer, primary_key = True)
   created_at = Column(DateTime(timezone = True), default = datetime.utcnow)
   modified_at = Column(DateTime(timezone = True), default = datetime.utcnow, onupdate = datetime.utcnow)

class User(Base, Abstract):
   __tablename__ = "user" # Table name
   # Table Fields
   name = Column(String(30), nullable = False)
   email = Column(String(80), nullable = False, unique = True)
   password = Column(LargeBinary, nullable = False)
   enc = Column(LargeBinary, nullable = False)
   is_verified = Column(Boolean, default = False)
   addresses = relationship("Address", back_populates = "user", lazy = "dynamic")
   cards = relationship("CreditCard", backref = "user")
   
   def __repr__(self):
      return f"User::(name = {self.name})"

class Address(Base, Abstract):
   __tablename__ = "address" # Table name
   # Table Fields
   line_1 = Column(String(80), nullable = False)
   line_2 = Column(String(50), nullable = False)
   city = Column(String(30), nullable = False)
   pin_code = Column(String(8), nullable = False)
   userID = Column(Integer, ForeignKey("user.ID"))
   user = relationship(User, back_populates = "addresses")
   
   def __repr__(self):
      return f"Address::(binded_to = {self.userID})"

class CreditCard(Base, Abstract):
   __tablename__ = "credit_card" # Table name
   # Table Fields
   card_type = Column(Enum(CardTypes), nullable = False)
   number = Column(String(19), nullable = False)
   holderID = Column(Integer, ForeignKey("user.ID"))
   
   def __repr__(self):
      return f"CreditCard::(holder = {self.holderID})"
