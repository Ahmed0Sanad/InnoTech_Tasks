# Script to sort dictionary by value
def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=not ascending))

sample_dict = {'apple': 45, 'banana': 30, 'cherry': 60, 'date': 25}

print("Original dictionary:", sample_dict)
print("Ascending order:", sort_dict_by_value(sample_dict, True))
print("Descending order:", sort_dict_by_value(sample_dict, False))