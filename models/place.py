#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table
import os


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
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
                            Column('place_id', String(60),
                                    ForeignKey('places.id'), nullable=False),
                            Column('amenity_id', String(60),
                                    ForeignKey('amenities.id'), nullable=False))
        amenity_ids = []

        reviews = relationship("Review", backref="place")
        amenities =\
            relationship("Amenity", secondary=place_amenity,
                        viewonly=False, backref="place_amenities")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

    @property
    def reviews(self):
        """
            Property reviews: reviews associated with place.id
        """
        reviews = storage.all(Review)
        my_reviews = []
        for review in reviews:
            if review.place_id == self.id:
                my_reviews.append(review)
        return my_reviews

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
