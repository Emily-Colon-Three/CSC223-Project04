import unittest
from basic_shape import BasicShape

# Tries to create a BasicShape object, which should raise a TypeError because it is an abstract class.
class ConstructBasicShape(unittest.TestCase):
    def test_basic_shape_construction(self):
        with self.assertRaises(TypeError):
            self.shape = BasicShape("Name", 0)