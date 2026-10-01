from abc import ABC, abstractmethod

class BasicShape(ABC):
    """BasicShape is an abstract class which serves as the base class for all shapes.
    Includes two properties, those being a name and an area, properties which all derived
    shape classes inherit. name is a string, while area is a float.
    Features one abstract method, the calc_area() method. Its behavior is specified by
    derived classes; it has no defined functionality in BasicShape."""

    # Constructor contains only the basic properties of all BasicShape derivatives.
    def __init__(self, name, area):
        self._name = name
        self._area = self.calc_area()

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, new: str):
        self._name = new

    @property
    def area(self) -> float:
        return self._area

    # calc_area() will be determined by derived classes; its functionality is undefined here.
    @abstractmethod
    def calc_area(self):
        pass