# create a simple countdown timer of 5 seconds using a while loop

import datetime
def timer(tim):
    while tim > 0:
        print(f"Time remaining: {tim} seconds")
        time.sleep(1)
        tim -= 1
    print("Time’s up!")

timer(5)