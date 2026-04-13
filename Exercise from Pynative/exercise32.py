# Practice Problem: Create a dictionary where the keys
# are numbers from 1 to 10 and the values
# are the squares of those numbers (e.g., 2: 4, 3: 9).

dic = {}

for i in range(1,11):
    j = i ** 2
    dic[i] = j
print(dic)
