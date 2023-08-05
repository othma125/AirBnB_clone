#!/usr/bin/python3
""" Module for test Base class """
import datetime

from models.base_model import BaseModel
from unittest import TestCase


class TestBaseMethods(TestCase):
    """ Suite to test BaseModel class """

    def setUp(self) -> None:
        """set up method"""
        self.Model = BaseModel()

    def test_attributes_types(self):
        """ Test assigned id """
        self.assertEqual(type(self.Model.id), str)
        self.assertEqual(type(self.Model.created_at), datetime.datetime)
        self.assertEqual(type(self.Model.updated_at), datetime.datetime)
        self.assertEqual(type(self.Model.id), str)
        self.assertTrue(self.Model.updated_at >= self.Model.created_at)

    def test_base_doc(self):
        """
        Tests for the doc string
        """
        import models.base_model as b
        self.assertIsNotNone(b.__doc__)
        self.assertFalse(b.__doc__ == '')
        self.assertIsNotNone(self.Model.__str__)
        self.assertFalse(self.Model.__str__ == '')
        self.assertIsNotNone(self.Model.to_dict)
        self.assertFalse(self.Model.to_dict.__doc__ == '')
        self.assertIsNotNone(self.Model.save)
        self.assertFalse(self.Model.save.__doc__ == '')
        # self.assertIsNotNone(base_model.__init__.__doc__)
        # self.assertFalse(base_model.__init__.__doc__ == '')
