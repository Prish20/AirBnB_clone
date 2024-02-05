import unittest
from datetime import datetime
from models.base_model import BaseModel

"""This is a test for the BaseModel class."""


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class."""
    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.model = BaseModel()

    def test_init(self):
        """Test the __init__ method of the BaseModel class."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """Test the save method of the BaseModel class."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of the BaseModel class."""
        expected_str = "[BaseModel] ({}) {}".format(self.model.id,
                                                    self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
