from basic_shape import BasicShape
import math

class Circle(BasicShape):
    """Circle is a shape class derived from the BasicShape base class. It imports math
    module for its area calculation.
    It features 3 unique properties, as well as the two properties of BasicShape. These
    are x_center, y_center, and radius, representing the coordinates to the center of the
    circle as well as its radius. All of these are of type float, with getter and setters.
    The setter for radius automatically updates the area property to match using the
    defined behavior of calc_area() for circle.
    calc_area() for Circle is defined as pi times radius squared. It returns the area of
    a circle, but does not update the area property inherently."""

    def __init__(self, x_center, y_center, radius, name = "Circle"):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

        super().__init__(name, self.calc_area()) # BasicShape properties and abstract method added here

    @property
    def x_center(self) -> float:
        return self._x_center
    @x_center.setter
    def x_center(self, new: float):
        self._x_center = new

    @property
    def y_center(self) -> float:
        return self._y_center
    @y_center.setter
    def y_center(self, new: float):
        self._y_center = new

    # Radius is the most special property, which is validated to always be positive and automatically recalculates the area with it.
    @property
    def radius(self) -> float:
        return self._radius
    @radius.setter
    def radius(self, new: float):
        if new <= 0.0:
            raise ValueError("radius must be greater than zero")

        self._radius = new
        self._area = self.calc_area()

    # formula for circle's area used; math module used for math.pi
    def calc_area(self) -> float:
        _area = math.pi * self._radius * self._radius
        return _area