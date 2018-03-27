#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates='state')

    @property
    def cities(self):
        '''
            Returns all cities associated with current state instance
        '''
        cities = [v for k,v in models.storage.all().items() if 'City' in k and v.state_id == self.id]

City.state = relationship("State", back_populates='cities')
