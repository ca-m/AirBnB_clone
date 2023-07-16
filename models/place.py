#!/usr/bin/python3
"""defines the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """represent a place

    Attributes:
        city_id (str): city id
        user_id (str): user id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms at the place
        number_bathrooms (int): number of bathrooms at the place
        max_guest (int): The maximum number of guests at the place
        price_by_night (int): price by night at the place
        latitude (float): place's latitude
        longitude (float): place's longitude
        amenity_ids (list): list of Amenity ids
    """

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
    amenity_ids = []
