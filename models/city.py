#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class City(BaseModel):
    '''
        Define the class City that inherits from BaseModel.
    '''
    state_id = ""
    name = ""
    places = relationship("Place", backref="cities")
