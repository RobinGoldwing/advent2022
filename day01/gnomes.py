#!/bin/env python3

# calculate the calories that each gnome carry
# all calories are written in "input.txt" file
# each gnome carry calories is sepparated by one space/carryLine

import math 

max_calories = 0
count_calories = 0

with open('input.txt') as file:
    for line in file.readlines():
        line = line.strip()
        if line == "":
            count_calories = 0
        else:
            count_calories += int(line)
            if count_calories >= max_calories:
                max_calories = count_calories
                count_calories = 0
            elif count_calories < max_calories:
                count_calories = 0
print("Max Calories : ", max_calories)
