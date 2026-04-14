from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class DealBase(BaseModel):
    product_id: Optional[int] = None
    promo_code: str
    description: str
    deal_type: str
    discount_percent: Optional[Decimal] = None
    buy_quantity: Optional[int] = None
    get_quantity: Optional[int] = None
    expiration_date: datetime


class DealCreate(DealBase):
    pass


class DealUpdate(BaseModel):
    product_id: Optional[int] = None
    promo_code: Optional[str] = None
    description: Optional[str] = None
    deal_type: Optional[str] = None
    discount_percent: Optional[Decimal] = None
    buy_quantity: Optional[int] = None
    get_quantity: Optional[int] = None
    expiration_date: Optional[datetime] = None


class Deal(DealBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
