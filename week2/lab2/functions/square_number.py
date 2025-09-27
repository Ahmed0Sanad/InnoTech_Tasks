# Function to square a number
def square_number(num):
    return num ** 2

number = float(input("Enter a number: "))
result = square_number(number)
print(f"The square of {number} is {result}")