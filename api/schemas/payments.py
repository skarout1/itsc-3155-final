from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    user_id: int
    order_id: int
    card_last_four: str
    card_brand: str
    payment_type: str
    transaction_status: str
    transaction_reference: str
    amount: Decimal


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    user_id: Optional[int] = None
    order_id: Optional[int] = None
    card_last_four: Optional[str] = None
    card_brand: Optional[str] = None
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    transaction_reference: Optional[str] = None
    amount: Optional[Decimal] = None


class Payment(PaymentBase):
    id: int
    paid_at: datetime

    class Config:
        from_attributes = True
