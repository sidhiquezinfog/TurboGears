from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Text

from wiki20.model import DeclarativeBase, metadata, DBSession

class Register(DeclarativeBase):
    __tablename__ = 'tbl_register'

    id = Column(Integer, primary_key=True,autoincrement=True)
    first_name = Column(String(25), nullable=False)
    user_name = Column(String(25), nullable=False)
    password = Column(String(25), nullable=False)
    email = Column(String(25), nullable=False)
    contact_no = Column(Integer, nullable=False)


