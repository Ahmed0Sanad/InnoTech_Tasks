# Program to reverse a string
def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"
reversed_string = reverse_string(sample_string)
print(f"Original: {sample_string}")
print(f"Reversed: {reversed_string}")