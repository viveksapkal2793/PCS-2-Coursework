
# Readme file

## Assignment 6: Deadlock Management

### Author

* Name: Vivek Sapkal

* Roll No.: B22AI066

### Description

This Python script simulates the Banker's algorithm for deadlock avoidance. It takes input data from a file, processes resource requests, and outputs the result to another file.


### Usage

* Ensure Python is installed on the system.
* Place your input data in the input.txt file according to the specified format in the files section below.
* Keep the input.txt file and bankers_algorithm.py file in the same directory.
* Run the the bankers_algorithm.py file.
* Check the output.txt file for the result of the simulation.


### Files

#### Bankers_algorithm.py

This python file contains the code for bankers algorithm. It reads input data from input.txt file and writes the result of the simulation to output.txt file.

#### Input File: (input.txt)

The input file contains the following sample data:

```text
5
3         
0 1 0   
2 0 0
3 0 2
2 1 1
0 0 2
7 5 3       
3 2 2
9 0 2
2 2 2
4 3 3
3 3 2       
```
The format of the data is as follows:

* 1 st line corresponds to no. of processes.
* 2 nd line corresponds to no. of resources.
* Next n lines will contain allocation matrix for n no. of processes.
* Next n lines will contain maximum demand matrix for n no. of processes.
* Last line will contain avalaible instances of each resource type.

#### Output File: (output.txt)

The output file will contain the result of the simulation. If the resource request is granted, it will display the safe sequence. Otherwise, it will indicate that the request was denied due to an unsafe state.

The output file will have the following data after running the program for above given sample input data:

```text
Request granted.
Safe sequence: 3 1 2 4 0
```


