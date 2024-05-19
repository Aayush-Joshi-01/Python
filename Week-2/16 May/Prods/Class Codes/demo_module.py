#city_list = ["indore", "delhi"]
import time

for remaining in range(10, 0, -1):
    print(remaining, end='', flush=True)
    time.sleep(1)
    print(end='\r')

print("Time's up!")