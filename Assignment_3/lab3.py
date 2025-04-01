import multiprocessing
import time
import random

class PCB:
    def __init__(self, process_id, program_counter, memory_limit):
        self.process_id = process_id
        self.program_counter = program_counter
        self.memory_limit = memory_limit
        self.state = "NEW"  # Initial state
        self.priority = random.randint(1, 10)  # Assign a random priority

    def set_state(self, new_state):
        self.state = new_state

def process_task(pcb):

    print(f"Process {pcb.process_id} with PID {multiprocessing.current_process().pid} is executing.")
    
    if random.uniform(0, 1) < 0.3: # 30% chance of process being completed (assumption for sake of simulation)
        time.sleep(random.uniform(0.1, 0.5)) # simulate processing time
        pcb.set_state("TERMINATED")
        print(f"Process {pcb.process_id} with PID {multiprocessing.current_process().pid} completed.")
    
    else:
        if random.uniform(0, 1) < 0.4:  # 40% chance of interruption (assumption for sake of simulation)
            time.sleep(random.uniform(0.1, 0.5)) # simulate processing time
            pcb.set_state("READY")
            print(f"Process {pcb.process_id} interrupted. Putting back in the ready queue.")
            ready_queue.put(pcb)
            return  # Process interrupted, exit function

        elif random.uniform(0, 1) < 0.2:  # 20% chance of waiting for I/O (assumption for sake of simulation)
            time.sleep(random.uniform(0.1, 0.5)) # simulate processing time
            pcb.set_state("WAITING")
            print(f"Process {pcb.process_id} waiting for I/O. Putting in the waiting queue.")
            io_waiting_queue.put(pcb)
            return  # Process waiting for I/O, exit function
        else:
            time.sleep(random.uniform(0.1, 0.5)) # simulate processing time
            pcb.set_state("TERMINATED")
            print(f"Process {pcb.process_id} with PID {multiprocessing.current_process().pid} completed.")

def long_term_scheduler(job_pool, ready_queue):
    processes = []

    # Retrieve processes from the job pool
    while not job_pool.empty():
        processes.append(job_pool.get())

    # Sort processes based on priority in descending order
    processes.sort(key=lambda x: x.priority, reverse=True)

    for pcb in processes:
        pcb.set_state("READY")
        ready_queue.put(pcb)

        # Simulate the scheduler making decisions based on priorities, etc.
        time.sleep(0.2)

def short_term_scheduler(ready_queue):
    try:
        while True:
            if not ready_queue.empty():
                pcb = ready_queue.get()
                pcb.set_state("RUNNING")

                process = multiprocessing.Process(target=process_task, args=(pcb,))
                process.start()
                process.join()

    except KeyboardInterrupt:
        print("Short-term scheduler terminated.")

# Define a function to handle waiting processes
def handle_waiting_processes(io_waiting_queue):
    while True:
        if not io_waiting_queue.empty():
            pcb = io_waiting_queue.get()
            pcb.set_state("READY")
            ready_queue.put(pcb)
            print(f"Process {pcb.process_id} moved from waiting to ready queue.")

if __name__== "__main__":
    num_processes = 7
    job_pool = multiprocessing.Queue()
    ready_queue = multiprocessing.Queue()
    io_waiting_queue = multiprocessing.Queue()

    # Enqueue processes into the job pool with varying program counters and memory limits
    for i in range(num_processes):
        program_counter = random.randint(100, 1000)
        memory_limit = random.randint(512, 2048)
        pcb = PCB(i, program_counter, memory_limit)
        job_pool.put(pcb)

    # Start the long-term scheduler in a separate process
    long_term_scheduler_process = multiprocessing.Process(target=long_term_scheduler, args=(job_pool, ready_queue))
    long_term_scheduler_process.start()

    # Start the short-term scheduler in a separate process
    short_term_scheduler_process = multiprocessing.Process(target=short_term_scheduler, args=(ready_queue,))
    short_term_scheduler_process.start()

    # Start the waiting process handler in a separate process
    waiting_handler_process = multiprocessing.Process(target=handle_waiting_processes, args=(io_waiting_queue,))
    waiting_handler_process.start()

    try:
        # Wait for the long-term scheduler and short-term scheduler processes to finish
        long_term_scheduler_process.join()
        short_term_scheduler_process.join()
        waiting_handler_process.join()
    except KeyboardInterrupt:
        print("Main process terminated.")

    print("Simulation completed.")