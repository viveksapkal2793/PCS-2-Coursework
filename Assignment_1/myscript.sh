#!/bin/bash
interval=3600
while true; do
	random_name=$(date +%s%N | md5sum | head -c 5)
	touch "${random_name}.txt"
	head -c 100 /dev/urandom | tr -dc 'a-zA-Z0-9' > ${random_name}.txt
	sleep $interval
done &
