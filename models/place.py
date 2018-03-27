#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    user = relationship("User", back_populates="places")
    place_amenity = Table('association', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
            )

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", "place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")
    else:
        reviews = storage.all(Review)
        my_reviews = []
        for review in reviews:
            if review.place_id == self.id:
                my_reviews.append(review)

"""
Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.
"""
    amenity_ids = []

        return my_reviews
