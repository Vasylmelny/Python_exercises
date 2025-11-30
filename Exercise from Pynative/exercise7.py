# Write a Python code to find how often the substring “Emma” appears in the given string.
#
# Given:
#
# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:
#
# Emma appeared 2 times

str_x = "Emma is good developer. Emma is a writer"

def emma(list):
    n = list.count("Emma")
    return n
print(f"Emma appeared {emma(str_x)} times")