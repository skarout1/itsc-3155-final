from datetime import datetime
from sqlalchemy import Column, DateTime, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    card_last_four = Column(String(4), nullable=False)
    card_brand = Column(String(50), nullable=False)
    payment_type = Column(String(50), nullable=False)
    transaction_status = Column(String(50), nullable=False)
    transaction_reference = Column(String(100), unique=True, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    paid_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("User", back_populates="payments")
    order = relationship("Order")
