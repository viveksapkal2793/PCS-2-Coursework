#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <path_to_filesystem>"
	exit 1
fi

# Function to display disk usage
check_disk_usage() {
    echo "Disk Usage:"
    df -h "$1"
    echo
    echo "File space usage:"
    du -h --max-depth=1 "$1"
}

# Function to display file count
check_file_count() {
    echo "File Count:"
    find "$1" -type f | wc -l
}

# Function to display directory count
check_directory_count() {
    echo "Directory Count:"
    find "$1" -type d | wc -l
}

# Main function
main() {

    filesystem_path="$1"

    echo "File System Report for: $filesystem_path"
    echo

    check_disk_usage "$filesystem_path"
    echo
    check_file_count "$filesystem_path"
    echo
    check_directory_count "$filesystem_path"
}

# Run the main function with the provided file system path
main "$1"
