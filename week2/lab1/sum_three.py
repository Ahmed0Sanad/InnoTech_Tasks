a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b or b == c or a == c:
    result = 0
else:
    result = a + b + c

print(f"Sum: {result}")