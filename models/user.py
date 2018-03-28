#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", back_populates="user")
    reviews = relationship("Review", back_populates="user")

    def __init__(self, *args, **kwargs):
        '''
            Initialize local variables
        '''
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(kwargs)
