# Write a code to swap keys and values in a dictionary.
# Assume all values are unique

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

new_dict = {}

for key, value in original_dict1.items():
    new_dict[value] = key

print(new_dict)

