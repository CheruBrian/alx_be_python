import math

class Shape:
    """Base class representing a generic geometric shape."""

    def area(self):
        """
        Abstract method to compute area.
        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize a rectangle with given length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with the given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle (π × r²)."""
        return math.pi * (self.radius ** 2)
