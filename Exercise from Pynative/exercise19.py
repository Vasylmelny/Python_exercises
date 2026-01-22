# don't finished!
def primenum(num):
    arr = []
    num1 = 1
    num2 = 2
    for i in range(1,num+1):
        arr.append(i)
        s = int(math.sqrt(i))
        for j in range(2,s+1):
            if i%j != 0:
                arr.remove(i)
                break
    print(arr)
# don't finished!
import math
primenum(20)