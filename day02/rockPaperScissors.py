#!/bin/env python3

# Rock Paper Scissors game
# Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the 
# outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# "The first column is what your opponent is going to play: 
# A for Rock, B for Paper, and C for Scissors. 

# The second column, you reason, must be what you should play in response: 
# X for Rock, Y for Paper, and Z for Scissors.

game_points = 0

with open('input.txt') as file:
    for line in file.readlines():
        line = line.split()
        if line[0] == 'A' and line[1] == 'X':
            game_points += 3
        elif line[0] == 'A' and line[1] == 'Y':
            game_points += 4
        elif line[0] == 'A' and line[1] == 'Z':
            game_points += 8
        elif line[0] == 'B' and line[1] == 'X':
            game_points += 1
        elif line[0] == 'B' and line[1] == 'Y':
            game_points += 5
        elif line[0] == 'B' and line[1] == 'Z':
            game_points += 9
        elif line[0] == 'C' and line[1] == 'X':
            game_points += 2
        elif line[0] == 'C' and line[1] == 'Y':
            game_points += 6
        elif line[0] == 'C' and line[1] == 'Z':
            game_points += 7

print(game_points)
        