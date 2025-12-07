# Perform following operations on given dictionary
#
# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary
# Expected Output:
#
# Original dictionary: {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#
# Updated dictionary after removing 'profession': {'name': 'Alice', 'age': 35, 'city': 'New York'}
#
# Printing all key-value pairs:
# name: Alice
# age: 35
# city: New York
#
# Does 'age' exist? True

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

print(f"Started dict is: {my_dict}")

my_dict.pop('profession')
print(f"Dict after deleting 'profession': {my_dict}")

print("printing all key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print(f"Does {"age"} exist? {"age" in my_dict.keys()}")