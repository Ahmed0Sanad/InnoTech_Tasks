# Circle class with area and perimeter methods
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Test the Circle class
circle = Circle(5)
print(f"Circle with radius {circle.radius}:")
print(f"Area: {circle.calculate_area():.2f}")
print(f"Perimeter: {circle.calculate_perimeter():.2f}")