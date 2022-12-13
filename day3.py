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

def FindDuplicatesPriorities(string1, string2):
    dic = {}
    for c1 in string1:
        for c2 in string2:
            if (c1 == c2):
                if (c1 not in dic):
                    dic[c1] = GetPriorityValue(c1)
    sumValue = 0
    for item in dic:
        sumValue += dic[item]

    return sumValue
    

def GetItemSum(inputfile):
    totalSum = 0
    for line in inputfile:
        size = len(line)
        halfsize = int(size/2)
        compartments = (line[0:halfsize], line[halfsize:size-1])
#        print("%d..%s" % (len(line), line))
        print ("(%s, %s)" % (compartments[0], compartments[1]))
        totalSum += FindDuplicatesPriorities(compartments[0], compartments[1])

    return totalSum

def main():
    with open("day3.input") as inputfile:
        print ("sum=%d" % GetItemSum(inputfile))
    
if __name__ == '__main__':
    main()
