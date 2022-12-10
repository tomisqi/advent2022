#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/2
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def GetPlayer2(player1, strategy):
    wins = {'R': 'P', 'P': 'S', 'S': 'R'}
    loses = {'R': 'S', 'P': 'R', 'S': 'P'}

    player2 = player1 # Draw
    if (strategy == 'X'): # Lose
        player2 = loses[player1]
    elif (strategy == 'Z'): # Win
        player2 =  wins[player1]
    return player2
        
def ToRPS(c):
    dic = {'A': 'R', 'B': 'P', 'C': 'S'}
    return dic[c]

def ToScore(strategy):
    dic = {'X': 0, 'Y': 3, 'Z': 6}
    return dic[strategy]

def ShapeValue(shape):
    dic = {'R': 1, 'P': 2, 'S': 3}
    return dic[shape]

def RpsScore(inputfile):
    totalScore = 0
    for line in inputfile:
        lineFields = line.split()
        player1 = ToRPS(lineFields[0])
        strategy = lineFields[1]
        player2 = GetPlayer2(player1, strategy)                
        score = ToScore(strategy) + ShapeValue(player2)
        print ("player1=%s player2=%s => %d" % (player1, player2, score))
        totalScore += score
    return totalScore

def main():
    with open("day2.input") as inputfile:
        print ("totalScore=%d" % RpsScore(inputfile))
    
if __name__ == '__main__':
    main()
