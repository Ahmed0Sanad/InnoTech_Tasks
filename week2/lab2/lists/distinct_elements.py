# Function to get distinct elements from list
def get_distinct_elements(lst):
    return list(set(lst))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_distinct_elements(sample_list)
print(f"Sample List : {sample_list}")
print(f"Unique List : {unique_list}")