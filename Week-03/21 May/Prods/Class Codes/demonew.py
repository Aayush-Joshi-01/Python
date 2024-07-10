import threading
import time


def timer():
    for i in range(10):
        time.sleep(1)
        print("\r", end="", flush=True)
        print(f"Timer: {i + 1} seconds have passed", end="", flush=True)


def other_code():
    here = input("Enter your answer: ")
    print(here)


# Create threads
timer_thread = threading.Thread(target=timer)
other_code_thread = threading.Thread(target=other_code)

# Start threads
timer_thread.start()
other_code_thread.start()

# Wait for threads to complete
timer_thread.join()
other_code_thread.join()

print("Both threads have finished execution")
