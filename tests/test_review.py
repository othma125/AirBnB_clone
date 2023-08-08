#!/usr/bin/python3
""" Module for test Review class """
from datetime import datetime
from io import StringIO
from unittest.mock import patch
from models.review import Review
from unittest import TestCase

class TestReviewMethods(TestCase):
    """Suite to test Review class"""
    def setUp(self) -> None:
        """set up method"""
        self.review = Review()

    def test_review_doc(self) -> None:
        """
        Tests for the doc string
        """
        import models.review as r

        self.assertIsNotNone(r.__doc__)
        self.assertFalse(r.__doc__ == "")
        self.assertIsNotNone(self.review.__str__)
        self.assertFalse(self.review.__str__ == "")
        self.assertIsNotNone(self.review.to_dict)
        self.assertFalse(self.review.to_dict.__doc__ == "")
        self.assertIsNotNone(self.review.save)
        self.assertFalse(self.review.save.__doc__ == "")
        self.assertIsNotNone(self.review.__init__.__doc__)
        self.assertFalse(self.review.__init__.__doc__ == "")

    def test_attributes_types(self) -> None:
        """Test assigned id"""
        self.assertEqual(type(self.review.id), str)
        self.assertEqual(type(self.review.created_at), datetime)
        self.assertEqual(type(self.review.updated_at), datetime)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)
        self.assertTrue(self.review.updated_at >= self.review.created_at)

    def test_read_from_dict(self) -> None:
        """Test read from dict"""
        my_dict = self.review.to_dict()
        self.assertEqual(type(my_dict), dict)
        output = "{"
        output += f"'place_id': '{self.review.place_id}'"
        output += f", 'user_id': '{self.review.user_id}'"
        output += f", 'text': '{self.review.text}'"
        output += f", 'id': '{self.review.id}'"
        output += f", 'created_at': '{self.review.created_at.isoformat()}'"
        output += f", 'updated_at': '{self.review.updated_at.isoformat()}'"
        output += f", '__class__': '{self.review.__class__.__name__}'"
        output += "}\n"
        with patch("sys.stdout", new=StringIO()) as out:
            print(my_dict)
            self.assertEqual(out.getvalue(), output)
        review = Review(**my_dict)
        self.assertIsNot(review, self.review)
        self.assertEqual(type(review.id), str)