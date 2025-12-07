# Use a lambda with the filter() function to get all even numbers from a list
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Expected Output:
#
# The even numbers in the list are: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

outnum = list(filter(lambda x : x % 2 == 0, numbers))
print(f'Even numbers from list are: {outnum}')