from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date

Base = declarative_base()

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    start_date = Column(Date)