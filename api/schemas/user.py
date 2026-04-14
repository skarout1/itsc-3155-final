from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str
    is_recurring_customer: bool = False


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    is_recurring_customer: Optional[bool] = None


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
