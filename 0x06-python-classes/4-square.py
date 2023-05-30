#!/usr/bin/python3

class Square:
    """Class representing a square
    """
    def __init__(self, size=0):
        """Init Square

        Attributes:
            size: length of side of square
        """
        self.size = size

    def area(self):
        """Find area of square

        Args:
            size (int): length of side of square

        Returns:
            int: area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter

        Returns:
            size (int): length of side of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter

        Args:
            value (int): natural number (>= 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
