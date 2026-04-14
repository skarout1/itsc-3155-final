from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    calories: int
    food_category: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    calories: Optional[int] = None
    food_category: Optional[str] = None


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
