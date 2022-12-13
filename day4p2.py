#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/4
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)


def IsOverlap(elf1, elf2):
    return not ((elf1[1] < elf2[0]) or (elf1[0] > elf2[1]))

def CountOverlapAssignments(inputfile):
    count = 0
    for line in inputfile:
        lineFields = line.rstrip("\n").split(",")
        tmp = lineFields[0].split("-")
        elf1 = (int(tmp[0]), int(tmp[1]))
        tmp = lineFields[1].split("-")
        elf2 = (int(tmp[0]), int(tmp[1]))
        print ("%s..%s -> %d" % (elf1, elf2, IsOverlap(elf1, elf2)))
        count += 1 if IsOverlap(elf1, elf2) else 0
    return count

def main():
    with open("day4.input") as inputfile:
        print ("count=%d" % CountOverlapAssignments(inputfile))
    
if __name__ == '__main__':
    main()
