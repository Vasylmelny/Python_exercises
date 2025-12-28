class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        square = self.radius ** 2 * 3.14
        return square

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        square = self.side ** 2
        return square

# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())