#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/9
'''

#NOTE! Check day9p2.py better for the better solution.

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def AddVector(pos, v):
    return [pos[0] + v[0], pos[1] + v[1]]

def ToVector(direction):
    if (direction == 'R'):
        return (1, 0)
    elif (direction == 'U'):
        return (0, 1)
    elif (direction == 'L'):
        return (-1, 0)
    elif (direction == 'D'):
        return (0, -1)
    else:
        assert(False)

def CalcDistance(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def SingleStep(pos, dest, v, visitedSet):
    iPos = pos
    if (v[0] != 0):
        iPos[1] = dest[1]
    if (v[1] != 0):
        iPos[0] = dest[0]
        
    dist = CalcDistance(pos, dest)
    for i in range(dist):
        iPos = AddVector(iPos, v)
        visitedSet.add(tuple(iPos))    

def VisitedPositions(inputfile):
    head = [0, 0]
    tail = [0, 0]
    visitedSet = set({tuple(tail)})
    for line in inputfile:
        lineFields = line.split()
        steps = int(lineFields[1])
        v = ToVector(lineFields[0])
        
        moveV = (steps*v[0], steps*v[1])
        prevHead = head
        prevTail = tail
        head = AddVector(head, moveV)
        if (CalcDistance(head, tail) > 1):
            moveV = ((steps-1)*v[0], (steps-1)*v[1])
            tail = AddVector(prevHead, moveV)
            SingleStep(prevTail, tail, v,  visitedSet)
            
    return len(visitedSet)

def main():
    with open("day9.input") as inputfile:
        print ("vistedPositions=%d" % VisitedPositions(inputfile))
    
if __name__ == '__main__':
    main()

