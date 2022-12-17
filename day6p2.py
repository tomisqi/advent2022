#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/6
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def Diff14Chars(line, start):
    s = set({})
    for i in range(14):
        s.add(line[start+i])
    result = len(s) == 14
    return result 

def FindMarker(inputfile):
    for line in inputfile:
        for i in range(len(line) - 14):
            if (Diff14Chars(line, i)):
                return i + 14
    return -1

def main():
    with open("day6.input") as inputfile:
        print ("marker=%d" % FindMarker(inputfile))
    
if __name__ == '__main__':
    main()

