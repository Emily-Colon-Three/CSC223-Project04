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

# Creates a Circle object, then runs tests on its area as properties are changed.
class CircleArea(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(1, -2, 5)

    def test_radius_change(self): # Tests that the initial area is correct, then changes the radius and tests new area.
        self.assertAlmostEqual(self.circle.area, (25 * math.pi))
        self.circle.radius = 4
        self.assertAlmostEqual(self.circle.area, (16 * math.pi))

    def test_coordinate_change(self): # Changes coordinates, tests area again to be unchanged.
        self.circle.x_center = 5
        self.circle.y_center = 2
        self.assertAlmostEqual(self.circle.area, (25 * math.pi))