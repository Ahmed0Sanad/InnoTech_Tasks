# Program to calculate volume of a sphere
import math

radius = float(input("Enter radius of sphere: "))
volume = (4/3) * math.pi * (radius ** 3)
print(f"Volume of sphere: {volume:.2f} cubic units")