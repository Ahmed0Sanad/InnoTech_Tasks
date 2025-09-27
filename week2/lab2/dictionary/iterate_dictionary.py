# Program to iterate over dictionaries using for loops
sample_dict = {'name': 'Alice', 'age': 25, 'profession': 'Engineer', 'city': 'Boston'}

print("Iterating over keys:")
for key in sample_dict:
    print(key)

print("\nIterating over values:")
for value in sample_dict.values():
    print(value)

print("\nIterating over key-value pairs:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")