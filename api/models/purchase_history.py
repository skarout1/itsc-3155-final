from datetime import datetime
from sqlalchemy import Column, DateTime, DECIMAL, ForeignKey, Integer
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class PurchaseHistory(Base):
    __tablename__ = "purchase_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    deal_id = Column(Integer, ForeignKey("deals.id"), nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)
    purchased_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="purchase_history")
    order = relationship("Order")
    product = relationship("Product", back_populates="purchase_history_entries")
    deal = relationship("Deal", back_populates="purchase_history_entries")
