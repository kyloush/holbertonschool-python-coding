#!/usr/bin/python3
'''create a square'''


class Square:
    '''with a size'''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    '''make the size value public'''

    def area(self):
        return self@Square
