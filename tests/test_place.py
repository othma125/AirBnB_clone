#!/usr/bin/python3
""" Module for test Place class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.place import Place
from unittest import TestCase

class TestPlaceMethods(TestCase):
    """Suite to test Place class"""
    def setUp(self) -> None:
        """set up method"""
        self.place = Place()

    def test_place_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.place as p

        self.assertIsNotNone(p.__doc__)
        self.assertFalse(p.__doc__ == "")
        self.assertIsNotNone(self.place.__str__)
        self.assertFalse(self.place.__str__ == "")
        self.assertIsNotNone(self.place.to_dict)
        self.assertFalse(self.place.to_dict.__doc__ == "")
        self.assertIsNotNone(self.place.save)
        self.assertFalse(self.place.save.__doc__ == "")
        self.assertIsNotNone(self.place.__init__.__doc__)
        self.assertFalse(self.place.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.place.id), str)
        self.assertEqual(type(self.place.created_at), datetime)
        self.assertEqual(type(self.place.updated_at), datetime)
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertTrue(self.place.updated_at >= self.place.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.place.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'city_id': '{self.place.city_id}'"
        output += f", 'user_id': '{self.place.user_id}'"
        output += f", 'name': '{self.place.name}'"
        output += f", 'description': '{self.place.description}'"
        output += f", 'number_rooms': {self.place.number_rooms}"
        output += f", 'number_bathrooms': {self.place.number_bathrooms}"
        output += f", 'max_guest': {self.place.max_guest}"
        output += f", 'price_by_night': {self.place.price_by_night}"
        output += f", 'latitude': {self.place.latitude}"
        output += f", 'longitude': {self.place.longitude}"
        output += f", 'amenity_ids': {self.place.amenity_ids}"
        output += f", 'id': '{self.place.id}'"
        output += f", 'created_at': '{self.place.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.place.updated_at.isoformat()}'"
        output += f", '__class__': '{self.place.__class__.__name__}'"
        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        place = Place(**my_dict)
        self.assertIsNot(place, self.place)
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)
        self.assertEqual(type(place.id), str)
        self.assertEqual(type(place.created_at), datetime)
        self.assertEqual(type(place.updated_at), datetime)
        self.assertTrue(place.updated_at >= place.created_at)

        
