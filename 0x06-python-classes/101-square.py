#!/usr/bin/python3
"""
Module 6-square
Defines a square class storing the size of its side,
        as well as a position offset
Checks for the size to be valid (uses getters and setters)
Checks for the position to be valid (uses getters and setters)
Can calculate area
Prints an ASCII representation of a square, applying position offset
"""


class Square:
    """Class representing a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Init Square

        Attributes:
            size: length of side of square
            position: offset of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter

        Returns:
            position (int, int): pair with both integers >= 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter

        Args:
            value (int, int): pair with both integers >= 0

        Returns:
            size (int): length of side of square

        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not (isinstance(value[0], int)
                 and
                 isinstance(value[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print out ASCII shape of square, with offset"""
        if (self.size == 0):
            print()
            return
        print("\n"*self.position[1], end="")
        for _ in range(self.size):
            print(f"{' '*self.position[0]}{'#'*self.size}")

    def __str__(self):
        _str = ""
        if (self.size == 0):
            return ""
        _str += "\n"*self.position[1]
        for _ in range(self.size - 1):
            _str += f"{' '*self.position[0]}{'#'*self.size}\n"
        _str += f"{' '*self.position[0]}{'#'*self.size}"
        return _str
