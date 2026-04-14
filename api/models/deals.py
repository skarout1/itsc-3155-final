from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String)
    discount_percent = Column(DECIMAL)