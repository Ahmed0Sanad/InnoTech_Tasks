# Shape class hierarchy with subclasses
import math

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclass must implement calculate_area")
    
    def calculate_perimeter(self):
        raise NotImplementedError("Subclass must implement calculate_perimeter")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        # Using Heron's formula
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side

# Test the shape classes
circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(4)

shapes = [circle, triangle, square]
shape_names = ["Circle", "Triangle", "Square"]

for shape, name in zip(shapes, shape_names):
    print(f"{name}:")
    print(f"  Area: {shape.calculate_area():.2f}")
    print(f"  Perimeter: {shape.calculate_perimeter():.2f}")