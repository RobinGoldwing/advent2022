#!/bin/env python

temp = [' ',' ',' ','m']

test = ()

with open('input.txt') as file:
    x = 0
    for line in file.readlines():
        for char in line:
            temp.append(char)
            temp.pop(0)
            x += 1
            #print(x, temp, sep = ' ')
            test = set(temp)
            if len(test) == len(temp):
                print(x)
                break