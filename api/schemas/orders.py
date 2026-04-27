from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_address: Optional[str] = None
    user_id: Optional[int] = None
    order_type: str = 'takeout'
    deal_id: Optional[int] = None
    total_price: Optional[float] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_address: Optional[str] = None
    user_id: Optional[int] = None
    order_type: Optional[str] = None
    order_status: Optional[str] = None
    deal_id: Optional[int] = None
    total_price: Optional[float] = None


class Order(OrderBase):
    id: int
    order_status: str
    tracking_number: str
    created_at: Optional[datetime] = None
    order_details: list[OrderDetail] = []

    class Config:
        from_attributes = True
