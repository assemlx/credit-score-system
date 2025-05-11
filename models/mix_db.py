from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class CreditMix(Base):
    __tablename__ = 'credit_mix'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    types_used = Column(Integer)
    total_types = Column(Integer)
