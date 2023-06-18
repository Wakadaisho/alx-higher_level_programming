#!/usr/bin/python3

"""
Module rectangle

Contains class definition for a rectangle model,
inheriting from Base
"""

from .base import Base


class Rectangle(Base):
    """Rectangle Model

    Methods:
        area() -> int
        display() -> None
        update(*args, **kwargs) -> None
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method - width property

        Raises:
            TypeError:  if width is not an integer
            ValueError: if width or height <= 0
        """
        if (type(value).__name__ != 'int'):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method - height property

        Raises:
            TypeError:  if height is not an integer
            ValueError: if height or height <= 0
        """
        if (type(value).__name__ != 'int'):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x property."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method - x property

        Raises:
            TypeError:  if x is not an integer
            ValueError: if x or height < 0
        """
        if (type(value).__name__ != 'int'):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y property."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method - y property

        Raises:
            TypeError:  if y is not an integer
            ValueError: if y or height < 0
        """
        if (type(value).__name__ != 'int'):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of a rectangle

        Returns:
            area (int)
        """
        return self.width * self.height

    def display(self):
        """Print out ASCII shape of rectangle, with an x, y offset"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print("{}{}".format(' ' * self.x, '#' * self.width))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
                )

    def update(self, *args, **kwargs):
        """Modify the attributes of an object instance
        In the order: id, width, height, x, y

        Args:
            args: None-keyworded arguments
            kwargs: keyword arguments
        """
        for i, value in enumerate(args):
            if (i == 0):
                self.width = value
            elif (i == 1):
                self.height = value
            elif (i == 2):
                self.x = value
            elif (i == 3):
                self.y = value
            elif (i == 4):
                self.id = value
            else:
                pass
        if (len(args) == 0 and kwargs is not None):
            for k, v in kwargs.items():
                if (k == "id"):
                    self.id = v
                elif (k == "width"):
                    self.width = v
                elif (k == "height"):
                    self.height = v
                elif (k == "x"):
                    self.x = v
                elif (k == "y"):
                    self.y = v
                else:
                    pass

    def to_dictionary(self):
        """Make a dictionary representation of a rectangle

        Returns:
            _dict: {id: int, width: int, height: int, x: int, y: int}
        """
        _dict = {}
        _dict['id'] = self.id
        _dict['width'] = self.width
        _dict['height'] = self.height
        _dict['x'] = self.x
        _dict['y'] = self.y
        return _dict

    def to_json(self):
        return self.to_dictionary()
