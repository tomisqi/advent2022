#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/10
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

OP_ADDX = 1
OP_NOOP = 2

def DecodeInstruction(lineFields):
    op = None
    opStr = lineFields[0]
    if (opStr == "addx"):
        op = OP_ADDX
    elif (opStr == "noop"):
        op = OP_NOOP
    else:
        assert(False)
    return (op, int(lineFields[1]) if op==OP_ADDX else 0)

def ReadProgram(inputfile):
    program = []
    for line in inputfile:
        lineFields = line.split()
        (op, value) = DecodeInstruction(lineFields)
        program.append((op, value))
    return program

def GetOpCode(op):
    return op[0]

def GetOpValue(op):
    return op[1]

def CycleDuration(opcode):
    result = 0
    if (opcode == OP_ADDX):
        result = 2
    elif (opcode == OP_NOOP):
        result = 1
    return result

def DrawCRT(program):
    pc = 0
    cycle = 1
    instrDone = cycle+CycleDuration(GetOpCode(program[0]))
    x = 1
    crt = 0
    programDone = False
    while (not programDone):
        if (cycle == instrDone):
            if (GetOpCode(program[pc]) == OP_ADDX):
                x += GetOpValue(program[pc])
            pc += 1
            if (pc < len(program)):
                instrDone = cycle + CycleDuration(GetOpCode(program[pc]))
            else:
                programDone = True

        if (crt >= (x - 1) and crt <= (x + 1)):
            print ("#", end='')
        else:
            print (".", end='')
       
        crt += 1
        if (cycle % 40 == 0):
            print ()
            crt = 0
        cycle += 1

def main():
    with open("day10.input") as inputfile:
        global program
        program = ReadProgram(inputfile)
        DrawCRT(program)
    
if __name__ == '__main__':
    main()

