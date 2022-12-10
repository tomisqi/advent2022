#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/2
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def GetWinner(play):
    if (play == 'RR' or play == 'PP' or play == 'SS'):
        return -1
    if ('R' in play and 'S' in play):
        return play.index('R')
    if ('P' in play and 'S' in play):
        return play.index('S')
    if ('R' in play and 'P' in play):
        return play.index('P')
    assert(False)

def GetRoundScore(player1, player2):
    # RR, AX, 11 -> 3
    # RP, AY, 12 -> 6
    # RS, AZ, 13 -> 0
    # PR, BX, 21 -> 0
    # PP, BY, 22 -> 3
    # PS, BZ, 23 -> 6
    # SR, CX, 31 -> 6
    # SP, CY, 32 -> 0
    # SS, CZ, 33 -> 3

    play = player1 + player2
    winner = GetWinner(play)
    
    score = 3
    if (winner == 0):
        score = 0
    if (winner == 1):
        score = 6
    
    return score

def ToRPS(c):
    dic = {'X': 'R', 'Y': 'P', 'Z': 'S', 'A': 'R', 'B': 'P', 'C': 'S'}
    return dic[c]

def ShapeValue(shape):
    dic = {'R': 1, 'P': 2, 'S': 3}
    return dic[shape]

def RpsScore(inputfile):
    totalScore = 0
    for line in inputfile:
        lineFields = line.split()
        player1 = ToRPS(lineFields[0])
        player2 = ToRPS(lineFields[1])
        score = GetRoundScore(player1, player2) + ShapeValue(player2)
        #print ("player1=%s player2=%s => %d" % (player1, player2, score))
        totalScore += score
    return totalScore

def main():
    with open("day2.input") as inputfile:
        print ("totalScore=%d" % RpsScore(inputfile))
    
if __name__ == '__main__':
    main()
