from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    user_id: int
    product_id: int
    score: int
    review_text: str


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    user_id: Optional[int] = None
    product_id: Optional[int] = None
    score: Optional[int] = None
    review_text: Optional[str] = None


class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
