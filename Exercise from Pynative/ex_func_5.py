# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself repeatedly.
#
# Expected Output:
#
# 55

def recur(num):
    if num == 0:
        return 0
    else:
        return num + recur(num - 1)

print(recur(10))