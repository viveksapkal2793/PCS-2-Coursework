import random
from collections import deque

class PageReplacementSimulator:
    """
    Simulates page replacement algorithms and calculates page faults.
    """

    def __init__(self, num_frames, page_reference_sequence):
        """
        Initializes the PageReplacementSimulator object.

        Parameters:
            num_frames (int): Number of frames in the memory.
            page_reference_sequence (list): Sequence of page references.
        """

        self.num_frames = num_frames
        self.page_reference_sequence = page_reference_sequence

    def fifo(self):
        """
        Simulates FIFO (First In, First Out) page replacement algorithm.

        Returns:
            tuple: Number of page faults and page fault percentage.
        """

        frames = deque(maxlen=self.num_frames)
        page_faults = 0

        for page in self.page_reference_sequence:

            if page not in frames:
                page_faults += 1

                if len(frames) == self.num_frames:
                    frames.popleft()

                frames.append(page)

        return page_faults, page_faults / len(self.page_reference_sequence) * 100

    def lru(self):
        """
        Simulates LRU (Least Recently Used) page replacement algorithm.

        Returns:
            tuple: Number of page faults and page fault percentage.
        """

        frames = []
        page_faults = 0

        for page in self.page_reference_sequence:

            if page not in frames:
                page_faults += 1

                if len(frames) == self.num_frames:
                    frames.pop(0)
                frames.append(page)

            else:
                frames.remove(page)
                frames.append(page)

        return page_faults, page_faults / len(self.page_reference_sequence) * 100

    def optimal(self):
        """
        Simulates Optimal page replacement algorithm.

        Returns:
            tuple: Number of page faults and page fault percentage.
        """

        frames = []
        page_faults = 0

        for i, page in enumerate(self.page_reference_sequence):

            if page not in frames:
                page_faults += 1

                if len(frames) == self.num_frames:
                    # Find the page that will not be used for the longest time

                    indexes = {p: self.page_reference_sequence[i:].index(p) if p in self.page_reference_sequence[i:] else float('inf') for p in frames}
                    page_to_replace = max(indexes, key=indexes.get)
                    frames.remove(page_to_replace)

                frames.append(page)

        return page_faults, page_faults / len(self.page_reference_sequence) * 100


def generate_realistic_page_reference_sequence(length, num_pages, locality_factor=0.4, locality_window=4):
    """
    Generates a realistic page reference sequence.

    Parameters:
        length (int): Length of the sequence.
        num_pages (int): Total number of pages.
        locality_factor (float): Factor determining the likelihood of high locality.
        locality_window (int): Size of the locality window.

    Returns:
        list: Generated page reference sequence.
    """

    sequence = []

    for _ in range(length):

        if random.random() < locality_factor and len(sequence) >= locality_window:
            # Generate page references with high locality
            start_index = max(0, len(sequence) - locality_window)
            page = random.choice(sequence[start_index:])

        else:
            # Generate page references with low locality
            page = random.randint(0, num_pages - 1)

        sequence.append(page)

    return sequence

def start_simulation(input_file=None, output_file=None):
    """
    Starts the simulation.

    Parameters:
        input_file (str): Path to the input file (optional).
        output_file (str): Path to the output file (optional).
    """

    if input_file:

        with open(input_file, 'r') as file:

            num_frames = int(file.readline().strip())
            num_sequences = int(file.readline().strip())

            page_reference_sequences = []
            for _ in range(num_sequences):

                page_reference_sequence = list(map(int, file.readline().strip().split(', ')))
                page_reference_sequences.append(page_reference_sequence)
    
    else:
        num_frames = 4
        num_sequences = 1
        num_pages = 10
        sequence_length = 50

        page_reference_sequence = generate_realistic_page_reference_sequence(sequence_length, num_pages)

    if output_file:
        output = open(output_file, 'w')

    for i in range(num_sequences):
            
        if input_file:
            page_reference_sequence = page_reference_sequences[i]
        else:
            page_reference_sequence = page_reference_sequence

        print("\nPage Reference Sequence:", page_reference_sequence)

        if output_file:
            output.write("Page Reference Sequence: {}\n".format(page_reference_sequence))

        # Initialize simulator
        simulator = PageReplacementSimulator(num_frames, page_reference_sequence)

        # Run simulations
        print("\nFIFO Page Replacement:")
        page_faults, fault_percentage = simulator.fifo()
        print("Page Faults:", page_faults)
        print("Page Fault Percentage:", fault_percentage, "%")

        if output_file:
            output.write("FIFO Page Replacement:\n")
            output.write("Page Faults: {}\n".format(page_faults))
            output.write("Page Fault Percentage: {} %\n".format(fault_percentage))

        print("\nLRU Page Replacement:")
        page_faults, fault_percentage = simulator.lru()
        print("Page Faults:", page_faults)
        print("Page Fault Percentage:", fault_percentage, "%")

        if output_file:
            output.write("LRU Page Replacement:\n")
            output.write("Page Faults: {}\n".format(page_faults))
            output.write("Page Fault Percentage: {} %\n".format(fault_percentage))

        print("\nOptimal Page Replacement:")
        page_faults, fault_percentage = simulator.optimal()
        print("Page Faults:", page_faults)
        print("Page Fault Percentage:", fault_percentage, "%")

        if output_file:
            output.write("Optimal Page Replacement:\n")
            output.write("Page Faults: {}\n".format(page_faults))
            output.write("Page Fault Percentage: {} %\n".format(fault_percentage))

    if output_file:
        output.close()

if __name__ == "__main__":

    files = True     # Set to True if input and output files are used, False for random generation
    input_file = "input.txt"  
    output_file = "output.txt"  

    if files:
        start_simulation(input_file, output_file)
    else:
        start_simulation()