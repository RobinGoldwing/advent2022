#!/bin/env python

# For the first few pairs, this list means:

# Within the first pair of Elves, the first Elf was assigned 
# sections 2-4 (sections 2, 3, and 4), while the second Elf was 
# assigned sections 6-8 (sections 6, 7, 8).
# The Elves in the second pair were each assigned two sections.
# The Elves in the third pair were each assigned three sections: 
# one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

# It seems like there is still quite a bit of duplicate work planned. 
# Instead, the Elves would like to know the number of pairs that overlap 
# at all.

# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5)
#  don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6,
#   and 2-6,4-8) do overlap:

# 5-7,7-9 overlaps in a single section, 7.
# 2-8,3-7 overlaps all of the sections 3 through 7.
# 6-6,4-6 overlaps in a single section, 6.
# 2-6,4-8 overlaps in sections 4, 5, and 6.
# So, in this example, the number of overlapping assignment pairs is 4.

# In how many assignment pairs do the ranges overlap?


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
        if int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):
            # print('True')
            miniCount += 1
        if int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1]):
            # print('True') 
            miniCount += 1
        if miniCount > 0:
            count += 1 
        miniCount = 0
print(count)