#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/5
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

def Pop(arr):
    elem = arr[-1]
    del arr[-1] # Modify the list in place (thanks GPT!)
    return elem

def Push(arr, elem):
    return arr.append(elem)

def Move(times, srcStack, dstStack):
    for i in range(times):
        Push(dstStack, Pop(srcStack))

def MoveOrdered(times, srcStack, dstStack):
    tmp = []
    Move(times, srcStack, tmp)
    Move(times, tmp, dstStack)

def DecodeMoveInstruction(lineFields):
    times = int(lineFields[1])
    srcStack = int(lineFields[3]) - 1 
    dstStack = int(lineFields[5]) - 1
    return (times, srcStack, dstStack)

def FindCratesAddToStack(line, stacks):
    for i in range(len(line)):
        c = line[i]
        if (c.isalpha()):
            stackIdx = i // 4
            if (stackIdx >= len(stacks)):
                # The stack in which this crate goes is beyond the stacks size. Expand it.
                delta = stackIdx - len(stacks) + 1
                for i in range(delta):
                    stacks.append([])
            stacks[stackIdx].append(c)
    
def FindTopCrates(inputfile):
    stacks = []
    for line in inputfile:
        lineFields = line.split()
        if (len(lineFields) == 0):
            # Drawin complete, but stacks have the crates in the reversed order.
            # Reverse it now.
            for stack in stacks:
                stack.reverse()
            print (stacks)
        elif (lineFields[0] == "move"):
            (times, src, dst) = DecodeMoveInstruction(lineFields)
            MoveOrdered(times, stacks[src], stacks[dst])
        else:
            # If it is not a move instruction, this is the stack drawing.
            FindCratesAddToStack(line, stacks)
    print ()
    print (stacks)
    
    topCratesStr = ""
    for stack in stacks:
        topCratesStr += stack[-1] if len(stack) > 0 else ""

    return topCratesStr

def main():
    with open("day5.input") as inputfile:
        print ("topCrates=%s" % FindTopCrates(inputfile))
    
if __name__ == '__main__':
    main()

