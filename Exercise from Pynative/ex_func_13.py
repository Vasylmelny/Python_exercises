# Write a recursive function to calculate the factorial of a non-negative integer.

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(5))
print(fac(7))
fac(8)
fac(9)
fac(10)