# Function to check if list is palindrome
def is_list_palindrome(lst):
    return lst == lst[::-1]

# Test cases
test_lists = [[1, 2, 3, 2, 1], [1, 2, 3, 4], ['a', 'b', 'a']]
for test_list in test_lists:
    result = is_list_palindrome(test_list)
    print(f"{test_list} is {'a palindrome' if result else 'not a palindrome'}")