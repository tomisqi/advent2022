#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/8
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def GetHeights2d(inputfile):
    heights2d = []
    for line in inputfile:
        heights2d.append(list(line.rstrip('\n')))

    cols = len(heights2d[0])
    rows = len(heights2d)
    for i in range(rows):
        for j in range(cols):
            heights2d[i][j] = int(heights2d[i][j])
        
    return heights2d

def Print2d(arr2d):
    cols = len(arr2d[0])
    rows = len(arr2d)
    print ("[%d, %d]=" % (rows, cols))
    for i in range(rows):
        print ("%02d)" % i, end = ' ')
        for j in range(cols):
            print ("%d" % (arr2d[i][j]), end='')
        print()

def CalculateScenicScore(treePos, heights2d):
    (x, y) = treePos
    tree = heights2d[y][x]
    
    cols = len(heights2d[0])
    rows = len(heights2d)

    up = 0 
    for i in reversed(range(0, y)):
        up += 1
        if (heights2d[i][x] >= tree):
            break

    down = 0 
    for i in range(y+1, rows):
        down += 1        
        if (heights2d[i][x] >= tree):
            break

    left = 0 
    for j in reversed(range(0, x)):
        left += 1
        if (heights2d[y][j] >= tree):
            break

    right = 0 
    for j in range(x+1, cols):
        right += 1
        if (heights2d[y][j] >= tree):
            break

#    print ("u=%d l=%d r=%d d=%d" % (up, left, right, down))
        
    return up * down * left * right

def MaxScenicScore(heights2d):
    cols = len(heights2d[0])
    rows = len(heights2d)

    Print2d(heights2d)

    maxScore = 0
    for i in range(1, rows - 1): # No need to check for edges since score is 0.
        for j in range(1, cols - 1):
            score = CalculateScenicScore((j, i), heights2d)
            maxScore = max(score, maxScore)
    return maxScore

def main():
    with open("day8.input") as inputfile:
        heights2d = GetHeights2d(inputfile)
        print ("maxScenicScore=%d" % MaxScenicScore(heights2d))
    
if __name__ == '__main__':
    main()
