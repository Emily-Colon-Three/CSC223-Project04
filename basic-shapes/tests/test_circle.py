import unittest
import math
from circle import Circle

# Creates basic and valid circle object, then tests to see that its area has been correctly set using assertAlmostEqual.
class ValidCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(0, 0, 1)

    def test_circle_area(self):
        self.assertAlmostEqual(self.circle.area, math.pi)

# Creates multiple circles which should raise the appropriate error; tests a series of invalid radii.
class InvalidCircles(unittest.TestCase):
    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            self.circle = Circle(0, 0, 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            self.circle = Circle(0, 0, -1)

    def test_non_number_radius(self):
        with self.assertRaises(TypeError):
            self.circle = Circle(0, 0, "One")
