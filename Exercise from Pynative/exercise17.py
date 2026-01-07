def fibonach(n):
    num1 = 0
    num2 = 1
    sum = 0
    print(num1)
    print(num2)
    while sum < n:
        print(sum)
        sum = num1 + num2
        num1 = num2
        num2 = sum

fibonach(10)
fibonach(20)
fibonach(400)