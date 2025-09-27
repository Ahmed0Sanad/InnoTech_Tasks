# Function to find kth largest element
def find_kth_largest(lst, k):
    if k <= 0 or k > len(lst):
        return None
    sorted_list = sorted(set(lst), reverse=True)
    return sorted_list[k-1] if k <= len(sorted_list) else None

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
k = 3
result = find_kth_largest(test_list, k)
print(f"List: {test_list}")
print(f"{k}rd largest element: {result}")