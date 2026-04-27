from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=True)
    customer_phone = Column(String(20), nullable=True)
    customer_address = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    order_type = Column(String(50), nullable=False, default='takeout')
    order_status = Column(String(50), nullable=False, default='pending')
    tracking_number = Column(String(36), unique=True, nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=True)
    deal_id = Column(Integer, ForeignKey("deals.id"), nullable=True)
    created_at = Column(DATETIME, default=datetime.now)

    user = relationship("User", back_populates="orders")
    deal = relationship("Deal")
    order_details = relationship("OrderDetail", back_populates="order")
