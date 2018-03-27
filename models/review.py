#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import relationship


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = "review"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(1024), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    user = relationship("User", back_populates="reviews")
