#!/udr/bin/python3
"""
This module defines the Place class, which inherits from BaseModel.

Place class represents a place that can be rented in the AirBnB clone project.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class for representing places in the AirBnB clone project.

    Attributes:
        city_id (str): ID of the city where the place is located.
        user_id (str): ID of the user who owns the place.
        name (str): Name of the place.
        ...
        amenity_ids (list): List of amenity IDs associated with the place.
    """

    city_id = ""
    user_id = ""
    description = ""
    number_rooms = int
    number_bathrooms = int
    max_guest = int
    price_by_night = int
    latitude = float
    longitude = float
    amenity_ids = [""]
