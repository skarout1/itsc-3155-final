from datetime import datetime
from sqlalchemy import Column, DateTime, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    promo_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=False)
    deal_type = Column(String(50), nullable=False)
    discount_percent = Column(DECIMAL(5, 2), nullable=True)
    buy_quantity = Column(Integer, nullable=True)
    get_quantity = Column(Integer, nullable=True)
    expiration_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    product = relationship("Product", back_populates="deals")
    purchase_history_entries = relationship("PurchaseHistory", back_populates="deal")
