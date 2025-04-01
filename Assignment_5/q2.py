import threading
import time
import random

semaphore = threading.Semaphore(3)

shared_resource = []

def access_shared_resource(thread_id):
    global shared_resource

    time.sleep(random.uniform(0.5, 1.5))

    semaphore.acquire()

    print(f"Thread {thread_id}: Acquired the semaphore")
    
    data = f"Data from Thread {thread_id}"
    print(f"Thread {thread_id}: Accessing shared resource (Adding {data} to shared_resource)")
    shared_resource.append(data)

    time.sleep(random.uniform(1, 2))

    print(f"Thread {thread_id}: Released the semaphore")
    semaphore.release()

threads = []
for i in range(10):
    thread = threading.Thread(target=access_shared_resource, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished execution")
print("Final shared_resource contents:", shared_resource)