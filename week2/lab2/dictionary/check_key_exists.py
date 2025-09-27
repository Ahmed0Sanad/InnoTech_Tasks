# Script to check if key exists in dictionary
def check_key_exists(dictionary, key):
    return key in dictionary

sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
test_keys = ['name', 'salary', 'age']

for key in test_keys:
    exists = check_key_exists(sample_dict, key)
    print(f"Key '{key}' {'exists' if exists else 'does not exist'} in dictionary")