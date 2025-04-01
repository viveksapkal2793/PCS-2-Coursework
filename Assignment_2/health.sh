#!/bin/bash

# Function to display CPU usage
check_cpu() {
    echo "CPU Usage:"
    top -bn1
}

# Function to display memory usage
check_memory() {
    echo "Memory Usage:"
    free -m
}

# Function to display disk space
check_disk() {
    echo "Disk Space:"
    df -h
}

# Main function
main() {
    echo "System Health Check:"
    check_cpu
    echo
    check_memory
    echo
    check_disk
}

# Run the main function
main
