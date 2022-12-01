#!/bin/env python3

# all calories are written in "input.txt" file
# each gnome carry calories is sepparated by one space/carryLine
# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?

import math 

max_calories = []
total_max_calories = 0
count_calories = 0

with open('input.txt') as file:
    for line in file.readlines():
        if not line:
            break
        try:
            x = int(str(line.strip()))
            count_calories += x
        except:
            max_calories.append(count_calories)
            count_calories = 0
max_calories.sort(reverse=True)
print("Max Calories : ", max_calories)
total_max_calories = max_calories[0]+ max_calories[1]+max_calories[2]
print("Total calories", total_max_calories) 