from sqlalchemy import Column, Integer, String

from ...pkg.sqlalchemy import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    name = Column(String)
