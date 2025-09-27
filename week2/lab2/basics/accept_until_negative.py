# Program to accept numbers until negative number is entered
while True:
    number = float(input("Enter a number (negative to stop): "))
    if number < 0:
        print("Negative number entered. Stopping.")
        break
    print(f"You entered: {number}")