import numpy as np

# Part 1 Solutions

# 1. Get NumPy version and build configuration
print("1. NumPy Version and Configuration:")
print(f"NumPy version: {np.__version__}")
print("Build configuration:")
np.show_config()

# 2. Test whether none of the elements are zero
print("\n2. Test if none of elements are zero:")
arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"None are zero: {np.all(arr != 0)}")

# 3. Test if any elements are non-zero
print("\n3. Test if any elements are non-zero:")
arr = np.array([0, 0, 1, 0])
print(f"Array: {arr}")
print(f"Any non-zero: {np.any(arr != 0)}")

# 4. Test for finiteness
print("\n4. Test for finiteness:")
arr = np.array([1, 2, np.inf, np.nan, 5])
print(f"Array: {arr}")
print(f"Finite elements: {np.isfinite(arr)}")

# 5. Test for positive/negative infinity
print("\n5. Test for infinity:")
arr = np.array([1, np.inf, -np.inf, np.nan])
print(f"Array: {arr}")
print(f"Positive infinity: {np.isposinf(arr)}")
print(f"Negative infinity: {np.isneginf(arr)}")

# 6. Test for NaN
print("\n6. Test for NaN:")
arr = np.array([1, 2, np.nan, 4])
print(f"Array: {arr}")
print(f"NaN elements: {np.isnan(arr)}")

# 7. Element-wise comparison (greater, greater_equal, less, less_equal)
print("\n7. Element-wise comparisons:")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 2, 1, 5])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Greater: {np.greater(arr1, arr2)}")
print(f"Greater equal: {np.greater_equal(arr1, arr2)}")
print(f"Less: {np.less(arr1, arr2)}")
print(f"Less equal: {np.less_equal(arr1, arr2)}")

# 8. Element-wise comparison (equal, equal within tolerance)
print("\n8. Equal comparisons:")
arr1 = np.array([1.0, 2.0, 3.0])
arr2 = np.array([1.0, 2.1, 3.0])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Equal: {np.equal(arr1, arr2)}")
print(f"Close (tolerance): {np.allclose(arr1, arr2, atol=0.2)}")

# 9. Array of 10 zeros, 10 ones, 10 fives
print("\n9. Array of zeros, ones, and fives:")
arr = np.concatenate([np.zeros(10), np.ones(10), np.full(10, 5)])
print(f"Array: {arr}")

# 10. Array of integers from 30 to 70
print("\n10. Integers from 30 to 70:")
arr = np.arange(30, 71)
print(f"Array: {arr}")

# 11. Even integers from 30 to 70
print("\n11. Even integers from 30 to 70:")
arr = np.arange(30, 71, 2)
print(f"Array: {arr}")

# 12. 3x3 identity matrix
print("\n12. 3x3 identity matrix:")
identity = np.eye(3)
print(identity)

# 13. Random number between 0 and 1
print("\n13. Random number between 0 and 1:")
random_num = np.random.random()
print(f"Random number: {random_num}")

# 14. Vector from 15 to 55, print all except first and last
print("\n14. Vector 15-55, excluding first and last:")
arr = np.arange(15, 56)
print(f"Original: {arr}")
print(f"Excluding first and last: {arr[1:-1]}")

# 15. Create 3x4 array and iterate
print("\n15. 3x4 array iteration:")
arr = np.arange(12).reshape(3, 4)
print(f"Array:\n{arr}")
print("Iteration:")
for element in np.nditer(arr):
    print(element, end=' ')
print()

# 16. Vector of length 10, values evenly distributed between 5 and 50
print("\n16. Vector with evenly distributed values:")
arr = np.linspace(5, 50, 10)
print(f"Array: {arr}")

# 17. Vector 0-20, change sign of numbers 9-15
print("\n17. Vector 0-20, change sign 9-15:")
arr = np.arange(21)
print(f"Original: {arr}")
arr[(arr >= 9) & (arr <= 15)] *= -1
print(f"Modified: {arr}")

# 18. Multiply values of two vectors
print("\n18. Multiply two vectors:")
vec1 = np.array([1, 2, 3, 4])
vec2 = np.array([2, 3, 4, 5])
result = vec1 * vec2
print(f"Vector 1: {vec1}")
print(f"Vector 2: {vec2}")
print(f"Product: {result}")

# 19. 3x4 matrix filled with values 10-21
print("\n19. 3x4 matrix with values 10-21:")
matrix = np.arange(10, 22).reshape(3, 4)
print(matrix)

# 20. Find rows and columns of matrix
print("\n20. Matrix dimensions:")
print(f"Shape: {matrix.shape}")
print(f"Rows: {matrix.shape[0]}, Columns: {matrix.shape[1]}")

# 21. 5x5 zero matrix with diagonal 1,2,3,4,5
print("\n21. 5x5 matrix with diagonal values:")
matrix = np.zeros((5, 5))
np.fill_diagonal(matrix, [1, 2, 3, 4, 5])
print(matrix)

# 22. 3x3x3 array with arbitrary values
print("\n22. 3x3x3 array:")
arr = np.random.random((3, 3, 3))
print(arr)

# 23. Sum of all elements, each column, each row
print("\n23. Array sums:")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array:\n{arr}")
print(f"Sum of all elements: {np.sum(arr)}")
print(f"Sum of each column: {np.sum(arr, axis=0)}")
print(f"Sum of each row: {np.sum(arr, axis=1)}")

# 24. Inner product of two vectors
print("\n24. Inner product:")
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
inner_product = np.inner(vec1, vec2)
print(f"Vector 1: {vec1}")
print(f"Vector 2: {vec2}")
print(f"Inner product: {inner_product}")

# 25. Add vector to each row of matrix
print("\n25. Add vector to each row:")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
result = matrix + vector
print(f"Matrix:\n{matrix}")
print(f"Vector: {vector}")
print(f"Result:\n{result}")

# 26. Check if two arrays are equal
print("\n26. Array equality:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Equal: {np.array_equal(arr1, arr2)}")

# 27. Create 5x6 array filled with zeros
print("\n27. 5x6 zero array:")
arr = np.zeros((5, 6))
print(arr)

# 28. Sort array by row and column
print("\n28. Sort array:")
arr = np.array([[3, 1, 4], [2, 6, 5]])
print(f"Original:\n{arr}")
print(f"Sort by row:\n{np.sort(arr, axis=1)}")
print(f"Sort by column:\n{np.sort(arr, axis=0)}")

# 29. Extract numbers less and greater than specified number
print("\n29. Extract numbers:")
arr = np.array([1, 5, 10, 15, 20])
threshold = 10
less_than = arr[arr < threshold]
greater_than = arr[arr > threshold]
print(f"Array: {arr}")
print(f"Less than {threshold}: {less_than}")
print(f"Greater than {threshold}: {greater_than}")

# 30. Replace numbers equal, less, greater than given number
print("\n30. Replace numbers:")
arr = np.array([1, 5, 10, 15, 20])
threshold = 10
arr_copy = arr.copy()
arr_copy[arr_copy == threshold] = 99  # equal
arr_copy[arr_copy < threshold] = 0    # less
arr_copy[arr_copy > threshold] = 100  # greater
print(f"Original: {arr}")
print(f"Modified: {arr_copy}")

# 31. 4x4 array, swap first-last, second-third columns
print("\n31. Swap columns:")
arr = np.arange(16).reshape(4, 4)
print(f"Original:\n{arr}")
arr[:, [0, 3]] = arr[:, [3, 0]]  # swap first and last
arr[:, [1, 2]] = arr[:, [2, 1]]  # swap second and third
print(f"After swapping:\n{arr}")

# 32. Swap rows and columns in reverse order
print("\n32. Reverse rows and columns:")
arr = np.arange(12).reshape(3, 4)
print(f"Original:\n{arr}")
reversed_arr = arr[::-1, ::-1]
print(f"Reversed:\n{reversed_arr}")

# 33. Multiply two arrays element-by-element
print("\n33. Element-wise multiplication:")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[2, 3], [4, 5]])
result = arr1 * arr2
print(f"Array 1:\n{arr1}")
print(f"Array 2:\n{arr2}")
print(f"Element-wise product:\n{result}")