#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False, default="")

    else:
        name = ""

        @property
        def amenities(self):
            """
                Property amenities: amenities associated with place.id

                Setter validates obj is Amenity

                Parameter:
                    obj: object to append obj.id to amenity_ids
            """
            return Place.amenity_ids

        def amenities(self, obj):
            if type(obj) is Amenity:
                Place.amenity_ids.append(obj.id)

#    place_amenities = relationship(
#            "Place", secondary="place_amenity", back_populates="amenities")
