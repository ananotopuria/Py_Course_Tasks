import math


class Shape:

    def __init__(self, name):
        self.name = name

    def area(self):
        return None


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def print_area(shape):
    print(f"The area of the {shape.name} is: {shape.area()}")


if __name__ == "__main__":

    rectangle = Rectangle("Rectangle", 5, 10)
    circle = Circle("Circle", 7)
    print_area(rectangle)
    print_area(circle)
