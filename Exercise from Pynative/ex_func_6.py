# Create a program with nested functions to perform
# an addition calculation as follows:
#
# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that
# calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”

def out(a, b):
    def add(a, b):
        return a + b
    sum = add(a, b) + 5
    return sum

print(out(5, 6))
