# Generate dictionary of numbers and their squares
def generate_squares_dict(n):
    return {i: i**2 for i in range(1, n+1)}

n = int(input("Enter number of elements: "))
squares_dict = generate_squares_dict(n)
print(f"Dictionary of numbers and squares: {squares_dict}")