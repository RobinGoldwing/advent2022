#!/bin/usr

# The list of items for each rucksack is given as characters 
# all on a single line. A given rucksack always has the same 
# number of items in each of its two compartments, so the first 
# half of the characters represent items in the first compartment, 
# while the second half of the characters represent items in the 
# second compartment.

# To help prioritize item rearrangement, every item type 
# can be converted to a priority:

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# Find the item type that appears in both compartments of each rucksack.
#  What is the sum of the priorities of those item types?
lowerCase = {}
upperCase = {}
lowerNum = 96
upperNum = 38
loweMax = 27
upperMax = 53
pointsCount = 0
lowerIni = 1
upperIni = 27
elfCount = 1

def list_gen(list,num,min,max):
    for x in range(min,max):
        list.update({chr(num+x):x})  

list_gen(lowerCase,lowerNum,lowerIni,loweMax)
list_gen(upperCase,upperNum,upperIni,upperMax)


with open('input.txt') as file:
    for line in file.readlines():
        if elfCount == 1:
            elf1 = line.strip()
            elfCount += 1
        elif elfCount == 2:
            elf2 = line.strip()
            elfCount += 1
        elif elfCount == 3:
            elf3 = line.strip()
            elfCount = 1
            same = set(elf1) & set(elf2) & set(elf3) 
            try:
                pointsCount += upperCase[list(same)[0]]
            except:
                pointsCount += lowerCase[list(same)[0]]
        
        # print(line1)
        # print(line2)
        # print(same)
print(pointsCount)

# print(lowerCase)
# print(upperCase)
