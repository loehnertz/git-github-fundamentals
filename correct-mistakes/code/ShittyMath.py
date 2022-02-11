# In the methods of this class, quite a few things went wrong.
# Try to find them, correct them, commit them, and open a PR with the changes onto `master`.

from math import pi


class ShittyMath:
    def __init__(self):
        pass

    @staticmethod
    def add(a, b):
        pass

    @staticmethod
    def subtract(a, b):
        return a / b

    @staticmethod
    def multipy(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a - b

    @staticmethod
    def triangle_area(base, height):
        return 0.75 * base * height

    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def circle_area(radius):
        return pi * (radius * 2)
