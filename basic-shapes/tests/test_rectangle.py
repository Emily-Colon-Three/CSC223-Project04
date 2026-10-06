import unittest
from rectangle import Rectangle

# Creates a valid, ordinary rectangle object and validates its area.
class ValidRectangle(unittest.TestCase):
    def test_rectangle(self):
        self.rectangle = Rectangle(5, 7)
        self.assertAlmostEqual(self.rectangle.area, 35)

# Creates a rectangle with a negative length, then one with negative width, to test that ValueError thrown.
class InvalidRectangle(unittest.TestCase):
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(-2, 4)
            print(self.rectangle.length)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(1, -2)

# Creates simple Rectangle object, then changes its sides and validates that area was updated.
class RectangleDimensionUpdate(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(12, 3) # Area would be 36 here

    def test_change_length(self):
        self.rectangle.length = 24
        self.assertAlmostEqual(self.rectangle.area, 72)

    def test_change_width(self):
        self.rectangle.width = 6
        self.assertAlmostEqual(self.rectangle.area, 72)