#!/usr/bin/python
__version__ = '0.1'

'''
  https://adventofcode.com/2022/day/7
'''

import sys

def RED(skk): return "\033[91m{}\033[00m".format(skk)

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "%d %s" % (self.size, self.name)

class Dir:
    def __init__(self, name, parent=None):
        self.files = []
        self.name = name
        self.parent = parent

    def AddFile(self, f):
        self.files.append(f)

    def FindDir(self, dirName):
        for f in self.files:
            if ((type(f) is Dir) and f.name == dirName):
                return f
        assert(False)
        return None

    def CalculateSize(self):
        # Recursively calculate the size of this directory including subdirectories.
        size = 0
        for f in self.files:
            if ((type(f) is Dir)):
                size += f.CalculateSize()
            else:
                size += f.size
        return size

    def Print(self, level=0):
        # Recursively print the directory with indentation in subdirectories.
        indentLvl = level * 2
        indentation = " " * indentLvl
        print ("%s- %s (dir)" % (indentation, self.name))
        for f in self.files:
            if (type(f) is Dir):
                f.Print(level+1)
            else:
                print ("%s  - %s" % (indentation, f))

def IsCmd(lineFields):
    return lineFields[0] == "$"

def IsCmdCD(lineFields):
    return lineFields[1] == "cd"

def GetCmdCDDirName(lineFields):
    return lineFields[2]

def IsFileDir(lineFields):
    return lineFields[0] == "dir"

def GetFileDirName(lineFields):
    return lineFields[1]

def GetFileName(lineFields):
    return lineFields[1]

def GetFileSize(lineFields):
    return int(lineFields[0])

def BuildFileSystem(inputfile):
    currDir = None
    for line in inputfile:
        lineFields = line.split()
        if (IsCmd(lineFields)):
            if (IsCmdCD(lineFields)):
                dirName = GetCmdCDDirName(lineFields)
                if (dirName == ".."):
                    currDir = currDir.parent
                else:
                    currDir = currDir.FindDir(dirName) if currDir else Dir("/")
        else:
            if (IsFileDir(lineFields)):
                dirName = GetFileDirName(lineFields)
                f = Dir(dirName, parent=currDir)
            else:
                fileName = GetFileName(lineFields)
                fileSize = GetFileSize(lineFields)
                f = File(fileName, fileSize)
            currDir.AddFile(f)

    # Move to root
    while (currDir.parent != None):
        currDir = currDir.parent

    currDir.Print()

    return currDir


def FindSmallestDirToDelete(d, freeTarget, currMin):
    for f in d.files:
        if (type(f) is Dir):
            dirSize = f.CalculateSize()
            if (dirSize >= freeTarget):
                if (dirSize < currMin):
                    currMin = dirSize
                currMin = FindSmallesDirToDelete(f, freeTarget, currMin)
    return currMin


def main():
    with open("day7.input") as inputfile:
        root = BuildFileSystem(inputfile)
        used = root.CalculateSize()
        free = 70000000 - used
        freeTarget = 30000000 - free
        print ()
        print ("smallestSize=%d" % FindSmallestDirToDelete(root, freeTarget, sys.maxsize))
    
if __name__ == '__main__':
    main()
