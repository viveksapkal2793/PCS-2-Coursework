#!/bin/bash

# Directory to clean up
target_directory="/home/vivek/PCS_2/archives"

# Archive directory
archive_directory="/home/vivek/PCS_2/Assignment_2"

# Ensure the archive directory exists
mkdir -p "$archive_directory"

# Find and move files older than 30 days to the archive directory
find "$target_directory" -type f -mtime +30 -exec mv {} "$archive_directory" \;

echo "Cleanup complete."
