# Print Reverse Number Pattern

def rev(numb):
    for i in range (1, numb + 1):
        reve = numb - i
        for j in range(reve + 1):
            print(i, end = " ")
        print()

rev(5)