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
    for i in range(rows):
        print ("%02d)" % i, end = ' ')
        for j in range(cols):
            print ("%d" % (arr2d[i][j]), end='')
        print()

def VisibleTrees(heights2d):
    cols = len(heights2d[0])
    rows = len(heights2d)

    results2d = []
    for i in range(rows):
        results2d.append([])
        for j in range(cols):
            results2d[i].append(0)

    for i in range(1, rows-1):
        leftHighest = heights2d[i][0]
        rightHighest = heights2d[i][cols-1]
        for j in range(1, cols - 1):
            # Left compare
            treeHeight = heights2d[i][j]
            if (treeHeight > leftHighest):
                results2d[i][j] = 1
                leftHighest = treeHeight

            # Right compare
            treeHeight = heights2d[i][(cols-1)-j]
            if (treeHeight > rightHighest):
                results2d[i][(cols-1)-j] = 1
                rightHighest = treeHeight

    for j in range(1, cols-1):
        topHighest = heights2d[0][j]
        bottomHighest = heights2d[rows-1][j]
        for i in range(1, rows - 1):
            # Top compare
            treeHeight = heights2d[i][j]
            if (treeHeight > topHighest):
                results2d[i][j] = 1
                topHighest = treeHeight

            # Bottom compare
            treeHeight = heights2d[(rows-1)-i][j]
            if (treeHeight > bottomHighest):
                results2d[(rows-1)-i][j] = 1
                bottomHighest = treeHeight

    Print2d(heights2d)
    print ()
    Print2d(results2d)    

    edge = (rows-2)*2 + (cols-2)*2 + 4
    interior = 0
    for i in range(rows):
        for j in range(cols):
            interior += results2d[i][j]
            
    return edge + interior

def main():
    with open("day8.input") as inputfile:
        heights2d = GetHeights2d(inputfile)
        print ("visibleTrees=%d" % VisibleTrees(heights2d))
    
if __name__ == '__main__':
    main()
