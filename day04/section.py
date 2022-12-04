#!/bin/env python

# For the first few pairs, this list means:

# Within the first pair of Elves, the first Elf was assigned 
# sections 2-4 (sections 2, 3, and 4), while the second Elf was 
# assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: 
# one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

count = 0
miniCount = 0
miniCount2 = 0

with open('input.txt') as file:
    for line in file.readlines():
        elfs = line.strip().split(',')
        elf1 = elfs[0].split('-')
        elf2 = elfs[1].split('-')
        # print(line)
        # print(elfs)
        # print(elf1)
        # print(elf2)
        if int(elf1[0]) <= int(elf2[0]):
            # print('True')
            miniCount += 1
        if int(elf1[1]) >= int(elf2[1]):
            # print('True') 
            miniCount += 1
        if int(elf2[0]) <= int(elf1[0]):
            # print('True')
            miniCount2 += 1
        if int(elf2[1]) >= int(elf1[1]):
            # print('True')
            miniCount2 += 1
        # print(miniCount)
        if miniCount == 2 or miniCount2 ==2:
            count += 1 
        miniCount = 0
        miniCount2 = 0
print(count)