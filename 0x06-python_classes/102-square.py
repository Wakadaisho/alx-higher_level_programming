#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, value):
        return self.area() == value.area()

    def __neq__(self, value):
        return self.area() != value.area()

    def __lt__(self, value):
        return self.area() < value.area()

    def __le__(self, value):
        return self.area() <= value.area()

    def __gt__(self, value):
        return self.area() > value.area()

    def __ge__(self, value):
        return self.area() >= value.area()
