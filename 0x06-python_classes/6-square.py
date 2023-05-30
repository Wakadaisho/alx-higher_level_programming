#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not (isinstance(position[0], int)
                 and
                 isinstance(position[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not (isinstance(value[0], int)
                 and
                 isinstance(value[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        print("\n"*self.__position[1], end="")
        for _ in range(self.__size):
            print(f"{' '*self.__position[0]}{'#'*self.__size}")
        if (self.__size == 0):
            print()
