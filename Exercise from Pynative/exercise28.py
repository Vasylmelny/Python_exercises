# Start with a list of 10 numbers.
# Iterate through them and sort them into two separate lists:
# one for even numbers and one for odd numbers.

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f"Eeven numbers:{even}")
print(f"Odd numbers:{odd}")
