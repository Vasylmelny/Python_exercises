# Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536,
# the output shall be “6 3 5 7“, with a space separating the digits.

def rever(num):
    out = str(num)
    out = out[::-1]
    for x in out:
        print(x, end=" ")
    print()

rever(123)
rever(1234)
rever(1232)

# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")

