#!/usr/bin/python3

import unittest
from models.place import Place


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.new_user = Place()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.city_id, "")
        self.assertEqual(self.new_user.user_id, "")
        self.assertEqual(self.new_user.description, "")
        self.assertEqual(self.new_user.number_rooms, int)
        self.assertEqual(self.new_user.number_bathrooms, int)
        self.assertEqual(self.new_user.max_guest, int)
        self.assertEqual(self.new_user.price_by_night, int)
        self.assertEqual(self.new_user.latitude, float)
        self.assertEqual(self.new_user.amenity_ids, [""])

    def test_user_attribute(self):
        self.new_user.city_id = "435feaf"
        self.new_user.user_id = "fez5fz"
        self.new_user.description = "Great Place"
        self.new_user.number_rooms = 6
        self.new_user.number_bathrooms = 4
        self.new_user.max_guest = 6
        self.new_user.price_by_night = 300
        self.new_user.latitude = 9.145
        self.new_user.longitude = 25.54
        self.new_user.amenity_ids = ["353565", "f536zf4", "4daz53"]

        self.assertEqual(self.new_user.city_id, "435feaf")
        self.assertEqual(self.new_user.user_id, "fez5fz")
        self.assertEqual(self.new_user.description, "Great Place")
        self.assertEqual(self.new_user.number_rooms, 6)
        self.assertEqual(self.new_user.number_bathrooms, 4)
        self.assertEqual(self.new_user.max_guest, 6)
        self.assertEqual(self.new_user.price_by_night, 300)
        self.assertEqual(self.new_user.latitude, 9.145)
        self.assertEqual(self.new_user.longitude, 25.54)
        self.assertEqual(self.new_user.amenity_ids,
                         ["353565", "f536zf4", "4daz53"])


if __name__ == '__main__':
    unittest.main()
