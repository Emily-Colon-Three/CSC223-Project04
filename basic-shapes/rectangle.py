from encodings import undefined

from basic_shape import BasicShape

class Rectangle(BasicShape):
    """The Rectangle class is a class derived from BasicShape, representing a rectangle.
    It features two unique properties, those being length and width, simple floats. They
    each have a getter and setter. The setter for each has validation logic implemented to
    raise ValueError if a set value is less than or equal to 0, ensuring positive values.
    calc_area() is defined by the class as length times width, called in the constructor
    and inside the setters for both length and width.
    However, in the setter for length, there is a try and except for this update which
    stops calc_area() from being run if self._width has yet to be initialized."""

    def __init__(self, length, width, name = "Rectangle"):
        self.length = length
        self.width = width

        super().__init__(name, self.calc_area())

    @property
    def length(self) -> float:
        return self._length
    @length.setter
    def length(self, new: float):
        if new <= 0:
            raise ValueError("Length must be greater than 0")

        self._length = new

        # An issue needs to be prevented when automatically updating Rectangle area:
        # calc_area() needs both length and width to be initialized first, meaning a try/except block is needed to prevent issues.
        try:
            self._width  # Updates area when length changed.
        except AttributeError:
            pass
        else:
            self._area = self.calc_area()

    @property
    def width(self) -> float:
        return self._width
    @width.setter
    def width(self, new: float):
        if new <= 0:
            raise ValueError("Width must be greater than 0")

        self._width = new
        self._area = self.calc_area() # Updates area when width changed.

    # How Rectangle class defines its area; used whenever dimensions are updated and in initialization.
    def calc_area(self) -> float:
        _area = self._length * self._width
        return _area