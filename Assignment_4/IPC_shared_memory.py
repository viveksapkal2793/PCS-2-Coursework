import multiprocessing
from multiprocessing import shared_memory
import time

# counter which increments every 5 seconds
def process_1(shared_mem):
    try:
        while True:
            time.sleep(5)
            current_value = shared_mem.buf[0]
            current_value += 1
            shared_mem.buf[0] = current_value
            print("Process-1: Counter incremented to", current_value)
    except KeyboardInterrupt:
        print("Process-1 Terminated")

# takes the value from counter and computes the square of that value
def process_2(shared_mem):
    try:
        while True:
            time.sleep(1)  # Check every second
            current_value = shared_mem.buf[0]
            square_value = current_value ** 2
            print("Process-2: Square of counter value", current_value, "is", square_value)
    except KeyboardInterrupt:
        print("Process-2 Terminated")

if __name__ == "__main__":
    # Create shared memory
    shared_mem = multiprocessing.shared_memory.SharedMemory(create=True, size=4)
    
    # Set the initial value in shared memory
    shared_mem.buf[0] = 0

    # Create processes
    p1 = multiprocessing.Process(target=process_1, args=(shared_mem,))
    p2 = multiprocessing.Process(target=process_2, args=(shared_mem,))
    
    # Start processes
    p1.start()
    p2.start()

    try:    
        # Join processes
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        # Close shared memory
        shared_mem.close()
        shared_mem.unlink()
        print("Processes Terminated !")