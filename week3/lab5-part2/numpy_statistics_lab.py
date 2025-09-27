import numpy as np

# NumPy Statistics LAB(5) - Part 2 Solutions

# 1. Find maximum and minimum value of a flattened array
print("1. Maximum and minimum of flattened array:")
arr = np.array([[0, 1], [2, 3]])
print(f"Original flattened array:\n{arr}")
print(f"Maximum value of the above flattened array:\n{np.max(arr)}")
print(f"Minimum value of the above flattened array:\n{np.min(arr)}")

# 2. Get min and max along second axis
print("\n2. Min and max along second axis:")
arr = np.array([[0, 1], [2, 3]])
print(f"Original array:\n{arr}")
print(f"Maximum value along the second axis:\n{np.max(arr, axis=1)}")
print(f"Minimum value along the second axis:\n{np.min(arr, axis=1)}")

# 3. Calculate difference between max and min along second axis
print("\n3. Difference between max and min along second axis:")
arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(f"Original array:\n{arr}")
diff = np.max(arr, axis=1) - np.min(arr, axis=1)
print(f"Difference between the maximum and the minimum values of the said array:\n{diff}")

# 4. Compute 80th percentile along second axis
print("\n4. 80th percentile along second axis:")
arr = np.array([[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0]])
print(f"Original array:\n{arr}")
percentile_80 = np.percentile(arr, 80, axis=1)
print(f"80th percentile along the second axis:\n{percentile_80}")

# 5. Compute median of flattened array
print("\n5. Median of flattened array:")
arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(f"Original array:\n{arr}")
median = np.median(arr)
print(f"Median of said array:\n{median}")

# 6. Compute weighted average
print("\n6. Weighted average:")
arr = np.array([0, 1, 2, 3, 4])
weights = np.array([1, 1, 1, 1, 2])
print(f"Original array:\n{arr}")
weighted_avg = np.average(arr, weights=weights)
print(f"Weighted average of the said array:\n{weighted_avg}")

# 7. Compute mean, std, and variance along second axis
print("\n7. Mean, standard deviation, and variance:")
arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(f"Original array:\n{arr}")
mean = np.mean(arr, axis=1)
std = np.std(arr, axis=1)
variance = np.var(arr, axis=1)
print(f"Mean along second axis: {mean}")
print(f"Standard deviation along second axis: {std}")
print(f"Variance along second axis: {variance}")

# 8. Compute covariance matrix
print("\n8. Covariance matrix:")
arr1 = np.array([0, 1, 2])
arr2 = np.array([2, 1, 0])
print(f"Original array1:\n{arr1}")
print(f"Original array2:\n{arr2}")
cov_matrix = np.cov(arr1, arr2)
print(f"Covariance matrix of the said arrays:\n{cov_matrix}")

# 9. Compute cross-correlation
print("\n9. Cross-correlation:")
arr1 = np.array([0, 1, 3])
arr2 = np.array([2, 4, 5])
print(f"Original array1:\n{arr1}")
print(f"Original array2:\n{arr2}")
cross_corr = np.correlate(arr1, arr2, mode='full')
print(f"Cross-correlation of the said arrays:\n{cross_corr}")

# 10. Compute Pearson correlation coefficients
print("\n10. Pearson correlation coefficients:")
arr1 = np.array([0, 1, 3])
arr2 = np.array([2, 4, 5])
print(f"Original array1:\n{arr1}")
print(f"Original array2:\n{arr2}")
corr_coeff = np.corrcoef(arr1, arr2)
print(f"Pearson product-moment correlation coefficients of the said arrays:\n{corr_coeff}")

# 11. Test element-wise for various conditions
print("\n11. Element-wise tests:")

# Test for finiteness
arr_finite = np.array([1, 2, np.inf])
print(f"Test element-wise for finiteness (not infinity or not Not a Number):")
print(np.isfinite(arr_finite))

# Test for infinity
arr_inf = np.array([np.inf, 1, -np.inf])
print(f"Test element-wise for positive or negative infinity:")
print(np.isinf(arr_inf))

# Test for NaN
arr_nan = np.array([np.nan, 1, 2])
print(f"Test element-wise for NaN:")
print(np.isnan(arr_nan))

# Test for NaT (Not a Time)
arr_nat = np.array(['2021-01-01', 'NaT'], dtype='datetime64')
print(f"Test element-wise for NaT (not a time):")
print(np.isnat(arr_nat))

# Test for negative infinity
arr_neginf = np.array([-np.inf, 1, 2])
print(f"Test element-wise for negative infinity:")
print(np.isneginf(arr_neginf).astype(int))

# Test for positive infinity
arr_posinf = np.array([1, 2, np.inf])
print(f"Test element-wise for positive infinity:")
print(np.isposinf(arr_posinf).astype(int))

# 12. Count occurrences using bincount
print("\n12. Count occurrences with bincount:")
arr = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])
print(f"Original array:\n{arr}")
counts = np.bincount(arr)
print(f"Number of occurrences of each value in array:\n{counts}")

# 13. Compute histogram
print("\n13. Compute histogram:")
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print(f"nums: {nums}")
print(f"bins: {bins}")
hist, bin_edges = np.histogram(nums, bins)
print(f"Result: (array({hist}), array({bin_edges}))")

