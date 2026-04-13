# Practice Problem: Print a downward number pattern where each row
# starts with a decreasing value.

Rows = 5

for i in range(Rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
