#!/usr/bin/python

import os
import sys

__debugging__ = False

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rotateRow(matrix, row, count):
    matrix[row] = matrix[row][count:] + matrix[row][:count] 

def convertMatrixToNumbers(matrix):
    for x in range(0, 4):
        for y in range(0, 4):
            matrix[x][y] = alphabet.index(matrix[x][y]) 

def convertMatrixToLetters(matrix):
    for x in range(0, 4):
        for y in range(0, 4):
            matrix[x][y] = alphabet[matrix[x][y]]

def computeRunningCount(matrix, runningCount):
    total = 0
    total = (matrix[0][0] + matrix[1][0] + matrix[2][0] + matrix[3][0]) % 26
    runningCount[0] = (runningCount[0] + total) % 26

    total = (matrix[0][1] + matrix[1][1] + matrix[2][1] + matrix[3][1]) % 26
    runningCount[1] = (runningCount[1] + total) % 26

    total = (matrix[0][2] + matrix[1][2] + matrix[2][2] + matrix[3][2]) % 26
    runningCount[2] = (runningCount[2] + total) % 26

    total = (matrix[0][3] + matrix[1][3] + matrix[2][3] + matrix[3][3]) % 26
    runningCount[3] = (runningCount[3] + total) % 26


def main(inputString):

    runningCount = [0, 0, 0, 0]
    matrix = [[0 for x in xrange(4)] for x in xrange(4)]

    if len(inputString) % 16 != 0:
        print "String length must be divisible by 16"
        return

    col = 0
    while col < len(inputString):
        row = -1
        for i in range(0, 16):
            if col % 4 == 0:
                row += 1
            matrix[row][col % 4] = inputString[col]
            col += 1

        convertMatrixToNumbers(matrix)
        
        if __debugging__:
            print matrix

        computeRunningCount(matrix, runningCount)

        if __debugging__:
            print runningCount

        rotateRow(matrix, 0, 1) 
        rotateRow(matrix, 1, 2) 
        rotateRow(matrix, 2, 3) 
        matrix[3].reverse()

        if __debugging__:
            print matrix

        computeRunningCount(matrix, runningCount)

        if __debugging__:
            print runningCount

    convertMatrixToLetters(matrix)

    print runningCount


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1].lower().replace(" ", ""))
    else:
        print "Wrong number of arguments"
