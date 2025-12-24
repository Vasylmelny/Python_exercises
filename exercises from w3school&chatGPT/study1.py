list1 = [23, 45, 17]
list2 = [1, 2, 3]

def result(list1, list2):
    reslist=[]
    for i in list1:
        if i % 2 == 1:
            reslist.append(i)
    for i in list2:
        if i % 2 == 0:
            reslist.append(i)
    return reslist

print(result(list1, list2))
