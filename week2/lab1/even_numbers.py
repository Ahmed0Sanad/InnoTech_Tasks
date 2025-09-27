n = int(input("Enter the upper limit: "))

print(f"Even numbers from 1 to {n}:")
for i in range(2, n + 1, 2):
    print(i, end=" ")
print()

# Alternative: Generate even numbers in a custom range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Even numbers between {start} and {end}:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")