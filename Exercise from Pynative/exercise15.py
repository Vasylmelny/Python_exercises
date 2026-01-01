def exponent(base, exp):
    if exp <= 0 or type(exp) != int or type(base) != int:
        raise TypeError("Exponent must be a positive integer")
    else:
        result = base ** exp
        print(f"{base} raises to the power of {exp} is: {result}")

exponent(2, 5)
exponent(5, 4)
# exponent(-5, -4)
# exponent(3.5, 2.4)