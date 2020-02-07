from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    level = Column(Integer())

    def __init__(self, name=None, level=0):
        self.name = "farima"
        self.level = 1

    def __repr__(self):
        return '<User %r>' % (self.name)