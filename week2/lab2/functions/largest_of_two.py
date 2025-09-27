# Function to return largest of two numbers
def largest_of_two(a, b):
    return a if a > b else b

# Test the function
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = largest_of_two(num1, num2)
print(f"The largest of {num1} and {num2} is {result}")