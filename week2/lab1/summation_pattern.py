n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    sum_val = sum(range(1, i + 1))
    numbers = " + ".join(str(j) for j in range(1, i + 1))
    print(f"{numbers} = {sum_val}")