# Program to determine number range
number = int(input("Enter an integer: "))

if 0 <= number <= 10:
    print("Range 1: 0 to 10")
elif 11 <= number <= 20:
    print("Range 2: 11 to 20")
elif 21 <= number <= 30:
    print("Range 3: 21 to 30")
elif 31 <= number <= 40:
    print("Range 4: 31 to 40")
else:
    print("Number is outside all specified ranges")