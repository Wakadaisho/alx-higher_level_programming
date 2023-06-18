#!/usr/bin/python3

"""
Module square

Contains class definition for a square model,
inheriting from Rectangle class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square Model"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                )

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        self.update(width=value, height=value)

    def update(self, *args, **kwargs):
        """Modify the attributes of an object instance
        In the order: id, size, x, y

        Args:
            args: None-keyworded arguments
            kwargs: keyword arguments
        """
        for i, value in enumerate(args):
            if (i == 0):
                self.width = value
                self.height = value
            elif (i == 1):
                self.x = value
            elif (i == 2):
                self.y = value
            elif (i == 3):
                self.id = value
            else:
                pass
        if (len(args) == 0 and kwargs is not None):
            for k, v in kwargs.items():
                if (k == "id"):
                    self.id = v
                elif (k == "size"):
                    self.width = v
                    self.height = v
                elif (k == "x"):
                    self.x = v
                elif (k == "y"):
                    self.y = v
                else:
                    pass

    def to_dictionary(self):
        """Make a dictionary representation of a square

        Returns:
            _dict: {id: int, size: int, x: int, y: int}
        """
        _dict = {}
        _dict['id'] = self.id
        _dict['size'] = self.width
        _dict['x'] = self.x
        _dict['y'] = self.y
        return _dict

    def to_json(self):
        return self.to_dictionary()
