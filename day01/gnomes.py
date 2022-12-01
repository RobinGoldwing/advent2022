#!/bin/env python3

# calculate the calories that each gnome carry
# all calories are written in "input.txt" file
# each gnome carry calories is sepparated by one space/carryLine

import math 

max_calories = 0
count_calories = 0

with open('input.txt') as file:
    for line in file.readlines():
        if not line:
            break
        try:
            x = int(str(line.strip()))
            count_calories += x
        except:
            if count_calories >= max_calories:
                max_calories = count_calories
                count_calories = 0
            elif count_calories < max_calories:
                count_calories = 0
print("Max Calories : ", max_calories)