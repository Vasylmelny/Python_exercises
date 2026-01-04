a = int(input("Enter a number: "))
b = a
rev = 0
while a > 0:
    rev = rev * 10 + a%10
    a = a // 10

print(rev)
if rev == b:
    print("The number ", a, "is a palindrome number")
else:
    print("The number ", a, "is not a palindrome number")
