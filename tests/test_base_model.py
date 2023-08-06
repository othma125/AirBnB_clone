#!/usr/bin/python3
""" Module for test Base class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from unittest import TestCase 

class TestBaseMethods(TestCase):
    """ Suite to test BaseModel class """

    def setUp(self) -> None:
        """set up method"""
        self.model = BaseModel()

    def test_base_model_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.base_model as b
        self.assertIsNotNone(b.__doc__)
        self.assertFalse(b.__doc__ == '')
        self.assertIsNotNone(self.model.__str__)
        self.assertFalse(self.model.__str__ == '')
        self.assertIsNotNone(self.model.to_dict)
        self.assertFalse(self.model.to_dict.__doc__ == '')
        self.assertIsNotNone(self.model.save)
        self.assertFalse(self.model.save.__doc__ == '')
        self.assertIsNotNone(self.model.__init__.__doc__)
        self.assertFalse(self.model.__init__.__doc__ == '')

    def test_attributes_types(self) -> None:
        """ Test assigned id """
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.model.created_at), datetime)
        self.assertEqual(type(self.model.updated_at), datetime)
        self.assertEqual(type(self.model.id), str)
        self.assertTrue(self.model.updated_at >= self.model.created_at)

    def test_read_from_dict(self) -> None:
        """ Test read from dict """
        my_dict = self.model.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = '{'
        output += f'\'id\': \'{self.model.id}\''
        output += f', \'created_at\': \'{self.model.created_at.isoformat()}\''
        output += f', \'updated_at\': \'{self.model.updated_at.isoformat()}\''
        output += f', \'__class__\': \'{self.model.__class__.__name__}\''
        output += '}\n'
        with patch('sys.stdout', new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        model = BaseModel(**my_dict)
        self.assertIsNot(model, self.model)
        self.assertEqual(type(model.id), str)
        self.assertEqual(type(model.created_at), datetime)
        self.assertEqual(type(model.updated_at), datetime)
        self.assertEqual(type(model.id), str)
        self.assertTrue(model.updated_at >= model.created_at)
        with patch('sys.stdout', new=StringIO()) as out:
            print(model.to_dict())
            self.assertEqual(out.getvalue(), output)
