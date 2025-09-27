# Function to check if string is palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for comparison
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Test cases
test_strings = ["madam", "nurses run", "hello", "A man a plan a canal Panama"]
for test in test_strings:
    result = is_palindrome(test)
    print(f"'{test}' is {'a palindrome' if result else 'not a palindrome'}")