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

def SignalStrength(program):
    pc = 0
    cycle = 1
    nextInstrDone = cycle+CycleDuration(GetOpCode(program[0]))
    x = 1
    ss = 0
    programDone = False
    while (not programDone):
        if (cycle == nextInstrDone):
            if (GetOpCode(program[pc]) == OP_ADDX):
                x += GetOpValue(program[pc])
            pc += 1
            if (pc < len(program)):
                nextInstrDone = cycle + CycleDuration(GetOpCode(program[pc]))
            else:
                programDone = True
        if (cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220):
            print (x)
            ss += x * cycle
        
        cycle += 1
    return ss

def main():
    with open("day10.input") as inputfile:
        global program
        program = ReadProgram(inputfile)
        print ("signalStrength=%d" % SignalStrength(program))
    
if __name__ == '__main__':
    main()

