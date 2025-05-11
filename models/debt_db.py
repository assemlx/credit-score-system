from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float

Base = declarative_base()

class Debt(Base):
    __tablename__ = 'debt'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    amount_used = Column(Float)
    credit_limit = Column(Float)
