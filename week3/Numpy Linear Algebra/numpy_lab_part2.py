import numpy as np

# Part 2 Solutions

# 1. Convert list to 1D NumPy array
print("1. Convert list to NumPy array:")
numeric_list = [12.23, 13.32, 100, 36.32]
arr = np.array(numeric_list)
print(f"Original List: {numeric_list}")
print(f"One-dimensional NumPy array: {arr}")

# 2. Create 3x3 matrix with values 2-10
print("\n2. 3x3 matrix with values 2-10:")
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)

# 3. Null vector of size 10, update 6th value to 11
print("\n3. Null vector, update 6th value:")
arr = np.zeros(10)
print(arr)
arr[5] = 11  # 6th element (0-indexed)
print("Update sixth value to 11")
print(arr)

# 4. Array with values 12-38
print("\n4. Array with values 12-38:")
arr = np.arange(12, 39)
print(arr)

# 5. Reverse an array
print("\n5. Reverse array:")
arr = np.arange(12, 38)
print(f"Original array:\n {arr}")
reversed_arr = arr[::-1]
print(f"Reverse array:\n {reversed_arr}")

# 6. Convert array to floating type
print("\n6. Convert to float:")
arr = [1, 2, 3, 4]
print(f"Original array:\n{arr}")
float_arr = np.array(arr, dtype=float)
print(f"Array converted to a float type:\n{float_arr}")

# 7. Append values to end of array
print("\n7. Append values:")
arr = np.array([10, 20, 30])
print(f"Original array:\n{arr}")
appended = np.append(arr, [40, 50, 60, 70, 80, 90])
print(f"After append values to the end of the array:\n{appended}")

# 8. Create empty and full array
print("\n8. Empty and full arrays:")
empty_arr = np.empty((3, 4))
print("Empty array:")
print(empty_arr)
full_arr = np.full((3, 3), 6)
print("Full array:")
print(full_arr)

# 9. Convert Celsius to Fahrenheit
print("\n9. Celsius to Fahrenheit conversion:")
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32
print(f"Sample Array {celsius.tolist()}")
print(f"Values in Fahrenheit degrees:\n{fahrenheit}")

celsius2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit2 = celsius2 * 9/5 + 32
print(f"Values in Centigrade degrees:\n{celsius2}")
print(f"Values in Fahrenheit degrees:\n{fahrenheit2}")

# 10. Test if elements of 1D array are present in second array
print("\n10. Test element presence:")
arr1 = np.array([0, 10, 20, 40, 60])
arr2 = [0, 40]
result = np.isin(arr1, arr2)
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Compare each element of array1 and array2\n{result}")

# 11. Find common values between two arrays
print("\n11. Common values:")
arr1 = np.array([0, 10, 20, 40, 60])
arr2 = [10, 30, 40]
common = np.intersect1d(arr1, arr2)
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Common values between two arrays:\n{common}")

# 12. Get unique elements
print("\n12. Unique elements:")
arr = np.array([10, 10, 20, 20, 30, 30])
print(f"Original array:\n{arr}")
unique = np.unique(arr)
print(f"Unique elements of the above array:\n{unique}")

arr2 = np.array([[1, 1], [2, 3]])
print(f"Original array:\n{arr2}")
unique2 = np.unique(arr2)
print(f"Unique elements of the above array:\n{unique2}")

# 13. Set difference between arrays
print("\n13. Set difference:")
arr1 = np.array([0, 10, 20, 40, 60, 80])
arr2 = [10, 30, 40, 50, 70, 90]
diff = np.setdiff1d(arr1, arr2)
print(f"Array1: {arr1}")
print(f"Array2: {arr2}")
print(f"Set difference between two arrays:\n{diff}")

# 14. Compare arrays using NumPy
print("\n14. Array comparisons:")
a = np.array([1, 2])
b = np.array([4, 5])
print(f"Array a: {a}")
print(f"Array b: {b}")
print(f"a > b\n{a > b}")
print(f"a >= b\n{a >= b}")
print(f"a < b\n{a < b}")
print(f"a <= b\n{a <= b}")

# 15. Sort along first and last axes
print("\n15. Sort along axes:")
arr = np.array([[4, 6], [2, 1]])
print(f"Original array:\n{arr}")
print(f"Sort along the first axis:\n{np.sort(arr, axis=0)}")
print(f"Sort along the last axis:\n{np.sort(arr, axis=1)}")

# 16. Values and indices bigger than 10
print("\n16. Values and indices > 10:")
arr = np.array([[0, 10, 20], [20, 30, 40]])
print(f"Original array:\n{arr}")
mask = arr > 10
values = arr[mask]
indices = np.where(mask)
print(f"Values bigger than 10 = {values}")
print(f"Their indices are {indices}")

# 17. Create contiguous flattened array
print("\n17. Flattened array:")
arr = np.array([[10, 20, 30], [20, 40, 50]])
print(f"Original array:\n{arr}")
flattened = arr.flatten()
print(f"New flattened array:\n{flattened}")

# 18. 2D array of size 2x3 with 4-byte integers
print("\n18. 2x3 array with 4-byte integers:")
arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print(f"Shape: {arr.shape}")
print(f"Type: {type(arr)}")
print(f"Data type: {arr.dtype}")

# 19. Reshape array without changing data
print("\n19. Reshape array:")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original shape: {arr.shape}")
reshaped_3x2 = arr.reshape(3, 2)
print(f"Reshape 3x2:\n{reshaped_3x2}")
reshaped_2x3 = reshaped_3x2.reshape(2, 3)
print(f"Reshape 2x3:\n{reshaped_2x3}")

# 20. Create 3x5 array filled with 2
print("\n20. 3x5 array filled with 2:")
arr = np.full((3, 5), 2)
print(arr)

# 21. Array of 10's with same shape and type
print("\n21. Array of 10's:")
original = np.array([1, 2, 3, 4])
tens = np.full_like(original, 10)
print(tens)

# 22. 2D array with diagonal [4,5,6,8]
print("\n22. Diagonal array:")
arr = np.diag([4, 5, 6, 8])
print(arr)

# 23. Arrays from 0-50 and 10-50
print("\n23. Arrays 0-50 and 10-50:")
arr1 = np.arange(50)
arr2 = np.arange(10, 50)
print(f"Array from 0 to 50:\n{arr1}")
print(f"Array from 10 to 50:\n{arr2}")

# 24. Find 4th element
print("\n24. 4th element:")
arr = np.array([[2, 4, 6], [6, 8, 10]])
print(arr)
fourth_element = arr.flat[3]  # 0-indexed, so 4th is index 3
print(f"Forth element of the array:\n{fourth_element}")

# 25. Test if specified values are present
print("\n25. Test value presence:")
arr = np.array([[1.12, 2., 3.45], [2.33, 5.12, 6.]])
print(f"Original array:\n{arr}")
print(np.any(arr == 2.))      # True
print(np.any(arr == 1.5))     # False  
print(np.any(arr == 6.))      # True
print(np.any(arr == 7.))      # False
print(np.any(arr == 1.12))    # True