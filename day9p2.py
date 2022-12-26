#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/9
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def AddVector(pos, v):
    return (pos[0] + v[0], pos[1] + v[1])

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
    # Simple calculation of distance.
    # Returns 1 if distance was sqrt(2) e.g.: (1,1) - (0,0).
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))
    
def PrintVisited(visited):
    minPos = [sys.maxsize, sys.maxsize]
    maxPos = [0, 0]
    for pos in visited:
        if (pos[0] < minPos[0]):
            minPos[0] = pos[0]
        if (pos[1] < minPos[1]):
            minPos[1] = pos[1]
        if (pos[0] > maxPos[0]):
            maxPos[0] = pos[0]
        if (pos[1] > maxPos[1]):
            maxPos[1] = pos[1]

    width  = maxPos[0] - minPos[0] + 1
    height = maxPos[1] - minPos[1] + 1

    for i in range(height):
        for j in range(width):
            (x, y) = (minPos[0] + j, minPos[1] + height - i - 1)
            print ("#" if (x, y) in visited else ".", end = '')
        print ()

def Head(body):
    return body[0]

def Tail(body):
    return body[-1]

def GetPieceMoveVector(head, piece):
    if (CalcDistance(head, piece) > 1):
        diffX = head[0] - piece[0]
        diffY = head[1] - piece[1]
        x = int(diffX / abs(diffX)) if diffX != 0 else 0
        y = int(diffY / abs(diffY)) if diffY != 0 else 0
        return (x, y)
    return (0, 0)

def MoveBody(body, headMoveVector):
    body[0] = AddVector(Head(body), headMoveVector)
    for i in range(1, len(body)):
        pieceMove = GetPieceMoveVector(body[i-1], body[i])
        body[i] = AddVector(body[i], pieceMove)

def DoSteps(body, visitedTail, steps, headVector):
    for i in range(steps):
        MoveBody(body, headVector)
        visitedTail.add(Tail(body))

def BuildBody(length):
    body = []
    for i in range(length):
        body.append((0, 0))
    return body

def VisitedPositions(inputfile):
    body = BuildBody(10)
    visitedTail = set()
    for line in inputfile:
        lineFields = line.split()
        steps = int(lineFields[1])
        headVector = ToVector(lineFields[0])
        DoSteps(body, visitedTail, steps, headVector)
    PrintVisited(visitedTail)
    return len(visitedTail)

def main():
    with open("day9.input") as inputfile:
        print ("vistedPositions=%d" % VisitedPositions(inputfile))
    
if __name__ == '__main__':
    main()

