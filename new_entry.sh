#!/bin/bash

year="$1"
day=$(printf "%02d" "$2")

createEntry() {
    day_path="./$year/$day"
    if [ -d "$day_path" ]; then
        echo "Entry already exists"
    else
        mkdir -p "$day_path"
        touch "$day_path/part1.py"
        touch "$day_path/part2.py"
        touch "$day_path/sample.txt"
        touch "$day_path/input.txt"
    fi
}

if [ -d "$year" ]; then
    createEntry
else
    mkdir -p "$year"
    createEntry
fi
