#!/usr/bin/python3
"""defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """represent a city

    Attributes:
        state_id (str): state id
        name (str): city name
    """

    state_id = ""
    name = ""
