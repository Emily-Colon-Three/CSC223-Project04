import unittest
from square import Square

# Creates a simple Square object with side length of 5. Ensures length, width, and side all equal.
class ValidSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_square(self):
        self.assertEqual(self.square.length, 5)
        self.assertEqual(self.square.width, 5)

        self.assertEqual(self.square.side, 5)

# Creates a Square object with side length 1, then doubles that and verifies dimensions are all updated accordingly.
class SquareSideUpdate(unittest.TestCase):
    def setUp(self):
        self.square = Square(1)

    def test_square_update(self):
        self.square.side = 2
        self.assertEqual(self.square.length, 2)
        self.assertEqual(self.square.width, 2)
        self.assertEqual(self.square.area, 4)

# Tests that attempting to solely set length or width of base class will use Square override to keep invariance.
class SquareLengthWidthUpdate(unittest.TestCase):
    def setUp(self):
        self.square = Square(3)

    def test_square_update_length(self):
        self.square.length = 5
        self.assertEqual(self.square.length, self.square.width, 5)
        self.assertEqual(self.square.area, 25)

    def test_square_update_width(self):
        self.square.width = 5
        self.assertEqual(self.square.length, self.square.width, 5)
        self.assertEqual(self.square.area, 25)

# Test which creates a Square object, then tries to set its side length to a negative value. Error is caught, and original value should remain unchanged.
class InvalidDimensionAssignment(unittest.TestCase):
    def setUp(self):
        self.square = Square(10)

    def test_side_invalid_assignment(self):
        with self.assertRaises(ValueError):
            self.square.side = -5
        self.assertEqual(self.square.side, 10)

if __name__ == '__main__':
    unittest.main()
