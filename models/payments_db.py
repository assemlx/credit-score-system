from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    on_time = Column(Integer)