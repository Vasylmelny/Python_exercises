# Write a Python program to create a new dictionary by extracting
# the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]


# print(sample_dict.keys())
# print(sample_dict.values())
new_dict = {}

for i in sample_dict.keys():
    for j in keys:
        if i == j:
            # print(sample_dict.keys(i))
            # print(sample_dict.values(i))
            # print(i, sample_dict[i])
            new_dict[j] = sample_dict[i]

print(new_dict)