# Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

for j in keys:
            sample_dict.pop(j)

print(sample_dict)