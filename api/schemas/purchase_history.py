from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class PurchaseHistoryBase(BaseModel):
    user_id: int
    order_id: int
    product_id: int
    deal_id: Optional[int] = None
    quantity: int
    unit_price: Decimal
    total_price: Decimal


class PurchaseHistoryCreate(PurchaseHistoryBase):
    pass


class PurchaseHistoryUpdate(BaseModel):
    user_id: Optional[int] = None
    order_id: Optional[int] = None
    product_id: Optional[int] = None
    deal_id: Optional[int] = None
    quantity: Optional[int] = None
    unit_price: Optional[Decimal] = None
    total_price: Optional[Decimal] = None


class PurchaseHistory(PurchaseHistoryBase):
    id: int
    purchased_at: datetime

    class Config:
        from_attributes = True
