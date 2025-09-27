# Function to count upper and lower case letters
def count_case_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

sample_string = 'The quick Brow Fox'
upper, lower = count_case_letters(sample_string)
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case Characters : {lower}")