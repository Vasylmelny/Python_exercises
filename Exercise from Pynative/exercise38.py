# Practice Problem: Create a countdown timer that starts
# from a given number and counts down to zero using a while loop.

import time

start_count = 5

while start_count > 0:
    print(start_count, end=" ")
    time.sleep(1)
    start_count -= 1

print("Blast off!")

