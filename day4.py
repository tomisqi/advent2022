#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/4
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)


def IsFullAssignment(elf1, elf2):
    minSection = min(elf1[0], elf2[0])
    maxSection = max(elf1[1], elf2[1])

    return (minSection == elf1[0] and maxSection == elf1[1]) or (minSection == elf2[0] and maxSection == elf2[1])

def CountFullAssignments(inputfile):
    count = 0
    for line in inputfile:
        lineFields = line.rstrip("\n").split(",")
        tmp = lineFields[0].split("-")
        elf1 = (int(tmp[0]), int(tmp[1]))
        tmp = lineFields[1].split("-")
        elf2 = (int(tmp[0]), int(tmp[1]))
        print ("%s .. %s -> %d" % (elf1, elf2, IsFullAssignment(elf1, elf2)))
        count += 1 if IsFullAssignment(elf1, elf2) else 0
    return count

def main():
    with open("day4.input") as inputfile:
        print ("count=%d" % CountFullAssignments(inputfile))
    
if __name__ == '__main__':
    main()
