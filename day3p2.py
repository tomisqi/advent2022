#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/3
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)


def GetPriorityValue(c):
    value = ord(c) - ord('A') + 27 if ord(c) < ord('a') else ord(c) - ord('a') + 1
    return value

def FindTriplicateItems(line0, line1, line2):
    dic = {}
    print ("%s %s %s" % (line0, line1, line2))
    for c0 in line0:
        found = False
        for c1 in line1:
            if ((c0 == c1) and (c0 not in dic)):
                for c2 in line2:
                    if (c0 == c2):
                        dic[c0] = GetPriorityValue(c0)
                        found = True
                        break
            if (found):
                break

    sumValue = 0
    for item in dic:
        sumValue += dic[item]

    return sumValue

def GetItemSum(inputfile):
    totalSum = 0
    lineCount = 0
    lines = ["", "", ""]
    for line in inputfile:
        if (lineCount % 3 == 0):
            totalSum += FindTriplicateItems(lines[0], lines[1], lines[2])
        lines[lineCount % 3] = line.rstrip('\n')
        lineCount += 1
    return totalSum

def main():
    with open("day3.input") as inputfile:
        print ("sum=%d" % GetItemSum(inputfile))
    
if __name__ == '__main__':
    main()
