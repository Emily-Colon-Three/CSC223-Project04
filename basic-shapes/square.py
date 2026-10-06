from rectangle import Rectangle

class Square(Rectangle):
    """Square is a class derived from the Rectangle class, having two base classes below
    it in the hierarchy. It is a rectangle with a single length for all sides, with equal
    length and width.
    It features a single unique property, side. Both the length and width from the base
    Rectangle class are set to this value, and must never not be equal to side.
    In order to prevent length or width from being set separately, the two properties are
    overridden in the class so that updated either will call side setter."""

    def __init__(self, side, name = "Square"):
        super().__init__(side, side, name)  # Rectangle base class initialization

        self._side = side

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, new: float):
        if new <= 0:
            raise ValueError("Side length must be greater than 0")

        self._side = new

        # Updates length and width to keep them both equal to side.
        self._length = self._side
        self._width = self._side
        self._area = self.calc_area()

    # Rectangle length and width setter overrides to maintain invariant
    @Rectangle.length.setter
    def length(self, new: float):
        self.side = new
    @Rectangle.width.setter
    def width(self, new: float):
        self.side = new