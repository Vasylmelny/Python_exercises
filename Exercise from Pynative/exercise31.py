# Practice Problem: Write a program to find all prime numbers up to 20,
# but only print every second (alternate) prime number found.

Limit = 20
result = []
res = []

for i in range(1,Limit+1):
    res.append(i)
    for j in range(2,i - 1):
        if i % j == 0:
            result.append(i)

sresult = set(result)
sres = set(res)

sr = sres.difference(sresult)
print(sr)

srl = list(sr)

rst =[]
for i in range(len(srl)):
    if i % 2 == 1:
        rst.append(srl[i])
        print(srl[i])

print(rst)
