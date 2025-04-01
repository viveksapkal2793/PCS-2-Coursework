#!/bin/bash

dir="/home/vivek/PCS_2/Assignment_1"

random_name=$(date +%s%N | md5sum | head -c 5)
random_file_name="${dir}/${random_name}.txt"

touch "$random_file_name"
head -c 100 /dev/urandom | tr -dc 'a-zA-Z0-9' > "$random_file_name" &
