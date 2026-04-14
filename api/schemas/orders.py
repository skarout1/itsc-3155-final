from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    user_id: int


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    user_id: Optional[int] = None


class Order(OrderBase):
    id: int
    created_at: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class Config:
        from_attributes = True
