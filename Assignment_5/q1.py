import threading
import time

NUM_THREADS = 2
NUM_EXECUTIONS = 5

flag = [False] * NUM_THREADS
turn = 0

shared_var = 0

def critical_section(thread_id):
    global shared_var

    for _ in range(NUM_EXECUTIONS):
        flag[thread_id] = True
        turn = 1 - thread_id

     
        while flag[1 - thread_id] and turn == 1 - thread_id:
            pass

        print(f"Thread {thread_id} entered critical section")
        shared_var += 1
        print(f"Thread {thread_id} modified shared variable to {shared_var}")

        time.sleep(1)  

        print(f"Thread {thread_id} exited critical section")
        flag[thread_id] = False

        print(f"Thread {thread_id} entered remainder section")
        time.sleep(0.5)  
        print(f"Thread {thread_id} exited remainder section")

if __name__ == "__main__":
    threads = []
    for i in range(NUM_THREADS):
        t = threading.Thread(target=critical_section, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Final value of shared variable:", shared_var)