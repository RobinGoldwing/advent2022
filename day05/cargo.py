#!/bin/env python

crate1 = []
crate2 = []
crate3 = []
crate4 = []
crate5 = []
crate6 = []
crate7 = []
crate8 = []
crate9 = []
crate = [None,crate1,crate2,crate3,crate4,crate5,crate6,crate7,crate8,crate9]

temp = []
list = []
crates = ''
origin = ''
destiny = ''

with open('input.txt') as file:
    x = 0
    for line in file.readlines():
        if x < 8:
            if (line[1:2] != " "):  crate[1].insert(len(crate1),line[1:2])  
            if (line[5:6] != " "):  crate[2].insert(len(crate2),line[5:6])
            if (line[9:10] != " "): crate[3].insert(len(crate3),line[9:10])
            if (line[13:14] != " "):crate[4].insert(len(crate4),line[13:14]) 
            if (line[17:18] != " "):crate[5].insert(len(crate5),line[17:18]) 
            if (line[21:22] != " "):crate[6].insert(len(crate6),line[21:22]) 
            if (line[25:26] != " "):crate[7].insert(len(crate7),line[25:26]) 
            if (line[29:30] != " "):crate[8].insert(len(crate8),line[29:30]) 
            if (line[33:34] != " "):crate[9].insert(len(crate9),line[33:34]) 
            x += 1
        elif x >= 8:
            if line[0] == 'm':
                list = line.split(' ')
                crates = int(list[1])
                origin = int(list[3])
                destiny = int(list[5])
                print(crates)
                print(origin, crate[origin], sep = ' ')
                print(destiny, crate[destiny],sep = ' ')
                for m in range (0,crates):
                    crate[destiny].insert(0,crate[origin][0])
                    crate[origin].pop(0)
                print(crate[origin])
                print(crate[destiny])


                


    
#crate1.reverse()
#print(crate)
print()
print(crate1)
print(crate2)
print(crate3)
print(crate4)
print(crate5)
print(crate6)
print(crate7)
print(crate8)
print(crate9)
