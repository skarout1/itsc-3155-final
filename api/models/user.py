from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=False)
    address = Column(String(255), nullable=False)
    is_recurring_customer = Column(Boolean, nullable=False, default=False)

    orders = relationship("Order", back_populates="user")
    purchase_history = relationship("PurchaseHistory", back_populates="user")
    payments = relationship("Payment", back_populates="user")
    reviews = relationship("Review", back_populates="user")
