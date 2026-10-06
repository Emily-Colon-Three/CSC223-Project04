import unittest
import math

from basic_shape import BasicShape
from rectangle import Rectangle
from circle import Circle
from square import Square

# Creates a list of various BasicShape derivatives, then runs tests on the list.
class MixedShapeList(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(1, -2, 3, "Circle 1")
        self.rectangle = Rectangle(11, 7, "Rectangle 1")
        self.square = Square(7, "Square 1")
        self.basic_shapes = [self.circle, self.rectangle, self.square]

    def test_if_instance(self): # Ensures all items in list are instance of BasicShape
        for shape in self.basic_shapes:
            self.assertIsInstance(shape, BasicShape)

    def test_name(self): # Goes through the name property of each element to verify correct name
        self.assertEqual(self.basic_shapes[0].name, "Circle 1")
        self.assertEqual(self.basic_shapes[1].name, "Rectangle 1")
        self.assertEqual(self.basic_shapes[2].name, "Square 1")

    def test_area(self): # Goes through the area property of each element, verifying correct respective area calculations
        self.assertAlmostEqual(self.basic_shapes[0].area, (9 * math.pi))
        self.assertEqual(self.basic_shapes[1].area, 77)
        self.assertEqual(self.basic_shapes[2].area, 49)

if __name__ == '__main__':
    unittest.main()
