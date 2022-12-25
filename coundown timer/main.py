import math
import time

enter_time = int(input("Enter the time in Min : ")) * 60

for i in range(enter_time, 0, -1):
    print(f"{int(i / 3600):02}:{math.floor(i / 60) % 60:02}:{i % 60:02}")
    time.sleep(1)
