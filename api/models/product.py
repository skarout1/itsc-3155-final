from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    calories = Column(Integer, nullable=False, default=0)
    food_category = Column(String(100), nullable=False)

    deals = relationship("Deal", back_populates="product")
    purchase_history_entries = relationship("PurchaseHistory", back_populates="product")
    reviews = relationship("Review", back_populates="product")
