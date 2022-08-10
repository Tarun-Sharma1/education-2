from datetime import datetime

from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Date, DateTime


class Item(Base):
    __tablename__ = 'education'
    aadhar = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    age = Column(Integer, nullable=False, unique=True)
    admissionno = Column(Integer)
    grade = Column(Integer)
    udise=Column(Integer)
    status = Column(Integer)

    def __repr__(self):
        return f"<Item name={self.name} udise={self.udise}>"
