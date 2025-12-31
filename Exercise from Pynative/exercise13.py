sum = int(input("Enter a number: "))
barysh = 0
if sum <= 10000:
    pass
else:
    first = sum - 10000
    if first <= 10000:
        barysh = first * 0.1
    else:
        second = first - 10000
        barysh += second * 0.2 + 1000
print(barysh)
