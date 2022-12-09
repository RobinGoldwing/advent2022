#!/bin/env python

root = {}
command = None
actual_dir = ''
storage = 0

def busca_size(diccionario, storage):
    for hijo in diccionario:
        for file in diccionario[hijo]:
            if type(diccionario[hijo][file]) == int:
                pass
            elif diccionario[hijo][file].isnumeric():
                if diccionario[hijo][file] == 'dirtotal':
                    pass
                else: 
                    diccionario[hijo]['dirtotal'] += int(diccionario[hijo][file])  
        if diccionario[hijo]['dirtotal'] <= 100000:
            print(diccionario[hijo]['parent']+' '+ diccionario[hijo]['name']+' dirtotal: '+str(diccionario[hijo]['dirtotal']))
            storage += (diccionario[hijo]['dirtotal'])
            print('\t'+ str(storage))
        


def read_file(root,actual_dir):
    with open('input.txt') as file:
        for line in file.readlines():
            command = line.strip().split(' ')
            if command[0] == '$':
                if command[1] == 'ls':
                    pass
                elif command[1] == 'cd':
                    if command[2] == '/':
                        actual_dir = command[2]
                        root[command[2]] = {}
                        root[command[2]]['name'] = command[2]
                        root[command[2]]['dirtotal'] = 0
                    elif command[2] == '..':
                        if actual_dir == '/':
                            pass
                        else:
                            actual_dir = root[actual_dir]['parent']
                        pass
                    elif command[2][0].isalpha():
                        parent = actual_dir 
                        actual_dir = command[2]
                        pass
                    else:
                        pass
                else:
                    pass
            elif command[0] == 'dir':
                if command[1] not in root.keys():
                    root[command[1]] = {}
                    root[command[1]]['parent'] = actual_dir
                    root[command[1]]['name'] = command[1]
                    root[command[1]]['dirtotal'] = 0
            elif command[0].isnumeric():
                root[actual_dir][command[1]] = command[0]
            else:
                pass 

read_file(root, actual_dir)
busca_size(root, storage)
print(root)
