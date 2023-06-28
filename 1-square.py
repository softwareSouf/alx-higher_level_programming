!/usr/bin/python3
class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def area(self):
        """Return the area of the square."""
        return self.size * self.size

    def perimeter(self):
        """Return the perimeter of the square."""
        return 4 * self.size
