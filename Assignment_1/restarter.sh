#!/bin/bash

while true; do

    if ! pgrep -x "myscript.sh" > /dev/null; then
	./myscript.sh &
    fi

    sleep 60
done &
