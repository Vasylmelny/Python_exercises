# Take two lists and find the elements that appear in both.
# Use Sets to perform the operation.

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

set1 = set(list_a)
set2 = set(list_b)

# 1 method
# set3 = set({})
#
# for item in set1:
#     if item in set2:
#         set3.add(item)

# 2 method
# set3 = set1.intersection(set2)

# 3 method
set3 = set1&set2

print(f"Common Elements:{set3}")