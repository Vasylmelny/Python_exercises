# Write a Python program to convert two Python lists into a dictionary
# where elements from the first list become keys and
# elements from the second list become values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

dictionary = dict(zip(keys, values))
print(dictionary)

# Second method
dict1 = {}
for i in range(len(values)):
    dict1.update({keys[i]:values[i]})

print(f"Dictionary is : {dict1}")