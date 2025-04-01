
# Readme File

## Assignment 7: Page Replacement Algorithm Simulator

### Author

* Name: Vivek Sapkal

* Roll No.: B22AI066

### Description

This Python program simulates three page replacement algorithms (FIFO, LRU, and Optimal) and analyzes their performance based on a given page reference sequence. It allows for either random generation of page reference sequences or reading input from a file.

### Implementation

The code consists of the following components:

* **PageReplacementSimulator Class:** 
This class contains implementations of the FIFO, LRU, and Optimal page replacement algorithms. It calculates the number of page faults and the page fault percentage for each algorithm.

* **generate_realistic_page_reference_sequence Function:** 
This function generates a realistic page reference sequence. It considers both high and low locality page references.

* **start_simulation Function:** 
This function starts the simulation process. It reads input from an input file if provided, otherwise generates random page reference sequences. It then runs simulations for each page replacement algorithm and prints the results. Optionally, it writes the results to an output file.


## Usage

Set the value of variable file to True to run the simulation using the data from input file and write the output to output file. 

Ensure that the input file is in same directory as the python file or else change the path of input_file variable in the program with the appropriate path to the input file.

To run the simulation, execute the python file with the following command:

```
python3 page_replacement_algos.py
```
### Files

#### page_replacement_algos.py

This python file contains the code for simulation of page replacement algorithms.

#### Input File: (input.txt)

If using an input file, provide the file path as an argument. The input file should have the following format:
 
```text
<num_frames>
<num_sequences>
<page_reference_sequence_1>
<page_reference_sequence_2>
...
```

The **sample input file** contains the following sample data:

```text
4
3
0, 7, 7, 4, 7, 7, 2, 9, 7, 0, 7, 0, 7, 6, 8, 3, 6, 6, 8, 1, 7, 6, 1, 1, 6, 4, 7, 1, 8, 6, 1, 0, 9, 4, 3, 0, 7, 6, 3, 6, 6, 6, 0, 6, 0, 5, 0, 0, 5, 2
8, 4, 4, 6, 4, 4, 4, 4, 9, 4, 4, 7, 7, 4, 4, 7, 4, 4, 4, 7, 9, 4, 6, 4, 9, 6, 8, 4, 6, 1, 7, 6, 4, 3, 5, 4, 4, 1, 5, 4, 1, 1, 4, 6, 1, 8, 9, 7, 9, 9
5, 9, 9, 5, 1, 5, 7, 1, 4, 5, 7, 5, 3, 8, 3, 8, 3, 9, 3, 9, 1, 5, 5, 1, 1, 7, 9, 0, 8, 0, 9, 0, 8, 5, 0, 0, 5, 5, 9, 4, 0, 0, 9, 4, 4, 7, 4, 4, 4, 4
```

#### Output File: (output.txt)

The program outputs the results of the simulations. If an output file is provided, the results are written to that file. The output includes the page reference sequences, number of page faults, and page fault percentages for each algorithm.

The **sample output file** will have the following data after running the program for above given sample input data:

```text
Page Reference Sequence: [0, 7, 7, 4, 7, 7, 2, 9, 7, 0, 7, 0, 7, 6, 8, 3, 6, 6, 8, 1, 7, 6, 1, 1, 6, 4, 7, 1, 8, 6, 1, 0, 9, 4, 3, 0, 7, 6, 3, 6, 6, 6, 0, 6, 0, 5, 0, 0, 5, 2]
FIFO Page Replacement:
Page Faults: 25
Page Fault Percentage: 50.0 %
LRU Page Replacement:
Page Faults: 22
Page Fault Percentage: 44.0 %
Optimal Page Replacement:
Page Faults: 17
Page Fault Percentage: 34.0 %
Page Reference Sequence: [8, 4, 4, 6, 4, 4, 4, 4, 9, 4, 4, 7, 7, 4, 4, 7, 4, 4, 4, 7, 9, 4, 6, 4, 9, 6, 8, 4, 6, 1, 7, 6, 4, 3, 5, 4, 4, 1, 5, 4, 1, 1, 4, 6, 1, 8, 9, 7, 9, 9]
FIFO Page Replacement:
Page Faults: 18
Page Fault Percentage: 36.0 %
LRU Page Replacement:
Page Faults: 15
Page Fault Percentage: 30.0 %
Optimal Page Replacement:
Page Faults: 12
Page Fault Percentage: 24.0 %
Page Reference Sequence: [5, 9, 9, 5, 1, 5, 7, 1, 4, 5, 7, 5, 3, 8, 3, 8, 3, 9, 3, 9, 1, 5, 5, 1, 1, 7, 9, 0, 8, 0, 9, 0, 8, 5, 0, 0, 5, 5, 9, 4, 0, 0, 9, 4, 4, 7, 4, 4, 4, 4]
FIFO Page Replacement:
Page Faults: 19
Page Fault Percentage: 38.0 %
LRU Page Replacement:
Page Faults: 16
Page Fault Percentage: 32.0 %
Optimal Page Replacement:
Page Faults: 12
Page Fault Percentage: 24.0 %
```



## Analysis



#### **FIFO Algorithm:**

* Strengths:
Simple to implement and understand.
Works well in scenarios where page accesses exhibit temporal locality.
* Weaknesses:
May suffer from the Belady's anomaly, where increasing the number of frames can unexpectedly increase the number of page faults.
Doesn't consider the future behavior of pages, leading to suboptimal eviction decisions.

#### **LRU Algorithm (Least Recently Used):**

* Strengths:
Tends to perform well in scenarios where the most recently used pages are likely to be used again soon.
Can capture both temporal and spatial locality in page accesses.
* Weaknesses:
Requires maintaining a history of page accesses, which can be computationally expensive.
Doesn't anticipate future page accesses, leading to suboptimal eviction decisions in some cases.

#### **Optimal Algorithm:**

* Strengths:
Theoretically, provides the best possible performance by evicting the page that will not be used for the longest time in the future.
Serves as an upper bound for comparison with other algorithms.
* Weaknesses:
Impractical for implementation in real systems due to the need for future knowledge of page accesses.
Requires significant computational resources to determine the optimal eviction decision.

## Results

* The analysis was done on the basis of following results obtained with number of frames as 4, 6 and 8.

| No. of Frames | Sequence | Algorithm | Page Faults | Page Fault Percentage |
|---------------|----------|-----------|-------------|-----------------------|
| 4             | 1        | FIFO      | 25          | 50.0%                 |
|               |          | LRU       | 22          | 44.0%                 |
|               |          | Optimal   | 17          | 34.0%                 |
|               |          |           |             |                       |
|               | 2        | FIFO      | 18          | 35.29%                |
|               |          | LRU       | 15          | 29.41%                |
|               |          | Optimal   | 12          | 23.53%                |
|               |          |           |             |                       |
|               | 3        | FIFO      | 19          | 38.0%                 |
|               |          | LRU       | 16          | 32.0%                 |
|               |          | Optimal   | 12          | 24.0%                 |
|               |          |           |             |                       |
| 6             | 1        | FIFO      | 17          | 34.0%                 |
|               |          | LRU       | 18          | 36.0%                 |
|               |          | Optimal   | 13          | 26.0%                 |
|               |          |           |             |                       |
|               | 2        | FIFO      | 13          | 25.49%                |
|               |          | LRU       | 11          | 21.57%                |
|               |          | Optimal   | 9           | 17.65%                |
|               |          |           |             |                       |
|               | 3        | FIFO      | 12          | 24.0%                 |
|               |          | LRU       | 12          | 24.0%                 |
|               |          | Optimal   | 9           | 18.0%                 |
|               |          |           |             |                       |
| 8             | 1        | FIFO      | 13          | 26.0%                 |
|               |          | LRU       | 12          | 24.0%                 |
|               |          | Optimal   | 11          | 22.0%                 |
|               |          |           |             |                       |
|               | 2        | FIFO      | 8           | 15.69%                |
|               |          | LRU       | 8           | 15.69%                |
|               |          | Optimal   | 8           | 15.69%                |
|               |          |           |             |                       |
|               | 3        | FIFO      | 8           | 16.0%                 |
|               |          | LRU       | 8           | 16.0%                 |
|               |          | Optimal   | 8           | 16.0%                 |

## Conclusion

#### Performance Variation: 
* The **performance** of all algorithms **improves** as the number of **frames increase**. 
* LRU usually performs better than FIFO. 
* Optimal algorithm consistently performs much better, especially as the number of frames increases, while FIFO and LRU exhibit higher page fault rates.

#### Trade-offs: 
* LRU strikes a balance between simplicity and performance, making it a practical choice in many scenarios. 
* FIFO, while simple, may suffer from performance issues due to its inability to adapt to changing access patterns. 
* Optimal algorithm provides best performance but is impractical for real-world implementation.