#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/6
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def Diff4Chars(line, start):
    s = set({line[start], line[start+1], line[start+2], line[start+3]})
    result = len(s) == 4
    print ("%s%s%s%s=%s" % (line[start], line[start+1], line[start+2], line[start+3], result))
    return result 

def FindMarker(inputfile):
    for line in inputfile:
        for i in range(len(line) - 4):
            if (Diff4Chars(line, i)):
                return i + 4
    return -1

def main():
    with open("day6.input") as inputfile:
        print ("marker=%d" % FindMarker(inputfile))
    
if __name__ == '__main__':
    main()

