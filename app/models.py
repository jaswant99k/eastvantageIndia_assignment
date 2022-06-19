from sqlalchemy import Column, Integer, String

from .db import Base

# model/table
class  Address(Base):
    __tablename__ = "address"

    # fields 
    id = Column(Integer,primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    phone_no = Column(String(20))
    email = Column(String(20))
    lat_lang = Column(String(50))