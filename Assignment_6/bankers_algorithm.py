class BankersAlgorithm:
    def __init__(self, n_processes, n_resources, allocation, max_demand, available):
        """
        Initializes the Banker's Algorithm with given parameters.

        Parameters:
        - n_processes: Number of processes in the system.
        - n_resources: Number of resource types in the system.
        - allocation: Matrix representing current resource allocation to processes.
        - max_demand: Matrix representing maximum resource demand of processes.
        - available: List representing available instances of each resource type.
        """

        self.n_processes = n_processes
        self.n_resources = n_resources
        self.allocation = allocation
        self.max_demand = max_demand
        self.available = available
        self.need = [[max_demand[i][j] - allocation[i][j] for j in range(n_resources)] for i in range(n_processes)]

    def is_safe_state(self, work, finish):
        """
        Checks if the system is in a safe state after resource allocation.

        Parameters:
        - work: List representing available instances of each resource type.
        - finish: List representing whether each process has finished or not.

        Returns:
        - Boolean indicating if the system is in a safe state.
        - List representing the safe sequence of processes.
        """

        work = work[:]
        finish = finish[:]
        sequence = []
        # repeatedly check for which processess should be allocated resources in a sequence which does not result in an unsafe state 
        while True:
            found = False
            for i in range(self.n_processes):
                if not finish[i] and all(need <= work for need, work in zip(self.need[i], work)):
                    work = [work[j] + self.allocation[i][j] for j in range(self.n_resources)]
                    finish[i] = True
                    sequence.append(i)
                    found = True
                    break
            if not found:
                break
        return all(finish), sequence

    def request_resources(self, process_id, request):
        """
        Requests resources for a process and checks if the request can be granted.

        Parameters:
        - process_id: ID of the process making the request.
        - request: List representing the resource request by the process.

        Returns:
        - Boolean indicating if the request was granted.
        - List representing the safe sequence of processes if granted, None otherwise.
        """

        if all(request[i] <= self.need[process_id][i] for i in range(self.n_resources)) \
                and all(request[i] <= self.available[i] for i in range(self.n_resources)):
            for i in range(self.n_resources):
                self.available[i] -= request[i]
                self.allocation[process_id][i] += request[i]
                self.need[process_id][i] -= request[i]

            finish = [False] * self.n_processes
            work = self.available[:]
            safe, sequence = self.is_safe_state(work, finish)

            if safe:
                return True, sequence
            else:
                # Rollback changes if requested allocation results in unsafe state
                for i in range(self.n_resources):
                    self.available[i] += request[i]
                    self.allocation[process_id][i] -= request[i]
                    self.need[process_id][i] += request[i]
                return False, None
        else:
            return False, None


def read_input_data(filename):
    """
    Reads input data from a text file.

    Parameters:
    - filename: Name of the input file containing system parameters.

    Returns:
    - Tuple containing the number of processes, number of resources, allocation matrix,
      maximum demand matrix, and available resources.
    """

    with open(filename, 'r') as file:
        lines = file.readlines()
        n_processes = int(lines[0])
        n_resources = int(lines[1])
        allocation = [[int(x) for x in lines[i].strip().split()] for i in range(2, 2 + n_processes)]
        max_demand = [[int(x) for x in lines[i].strip().split()] for i in range(2 + n_processes, 2 + 2 * n_processes)]
        available = [int(x) for x in lines[-1].strip().split()]
    return n_processes, n_resources, allocation, max_demand, available


def write_output_data(filename, granted, sequence):
    """
    Writes output data to a text file.

    Parameters:
    - filename: Name of the output file.
    - granted: Boolean indicating if the resource request was granted.
    - sequence: List representing the safe sequence of processes.
    """

    with open(filename, 'w') as file:
        file.write("Request granted.\nSafe sequence: " + " ".join(str(i) for i in sequence) if granted else "Request denied. Unsafe state detected.")


def main():
    """
    Main function to run the Banker's Algorithm simulation.
    """

    input_filename = 'input.txt'
    output_filename = 'output.txt'

    n_processes, n_resources, allocation, max_demand, available = read_input_data(input_filename)

    # initializing instance of bankers algorithm
    banker = BankersAlgorithm(n_processes, n_resources, allocation, max_demand, available)

    process_id = 4
    request = [0, 2, 0]

    # making a request for resources
    granted, sequence = banker.request_resources(process_id, request)

    write_output_data(output_filename, granted, sequence)

    if granted:
        print("Request granted. Safe sequence:", sequence)
    else:
        print("Request denied. Unsafe state detected.")


if __name__ == "__main__":
    main()