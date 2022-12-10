#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/1
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def MostCalories(inputfile):
    topElves = [0, 0, 0]
    elf = 1
    calories = 0
    for line in inputfile:
        if line != '\n':
            calories += int(line)
        else:
            if (calories > topElves[0]):
                topElves[0] = calories
                topElves.sort()
#            print ("%d %d" % (elf, calories))
            elf += 1
            calories = 0
    return topElves

def main():
    with open("day1.input") as inputfile:
        topElves = MostCalories(inputfile)
        print ("sum=%d (%s)" % (sum(topElves), topElves))
    
if __name__ == '__main__':
    main()
