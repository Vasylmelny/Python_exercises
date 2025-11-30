# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
#
# Expected Output:
#
# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome numberA

def palindr(num):
    a = list(str(num))
    n = len(a)
    if n%2 == 0:
        m = n/2
    else:
        m = n//2
    for x in range(m):
        if a[x] == a[n - x - 1]:
            pass
        else:
            print("given number is not palindrome number")
            break
        print("given number is palindrome number")

palindr(121)
palindr(12321)
palindr(12331)

# def is_palindrome(number):
#
#   # Handle negative numbers (they are typically not palindromes)
#   if number < 0:
#     return False
#
#   # Convert the number to a string
#   original_string = str(number)
#
#   # Reverse the string using slicing
#   reversed_string = original_string[::-1]
#
#   # Compare the original and reversed strings
#   if original_string == reversed_string:
#     return True
#   else:
#     return False