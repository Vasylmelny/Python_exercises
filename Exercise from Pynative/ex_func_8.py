def generator():
    # lis=[]
    # for i in range(4,30):
    #     if i % 2 == 0:
    #         lis.append(i)
    lis = [i for i in range(4, 30) if i % 2 == 0]
    print(lis)

generator()
