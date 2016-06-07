#!/usr/bin/python

import sys

def main():
    inputFile = open(sys.argv[1], 'r')
    outputFile = open('outfile', 'w')

    currLine = inputFile.readlines()
    column = 0
    columnLength = len(currLine[column]) - 1
    output = []
    while (column < columnLength):
        for row in range(0,len(currLine)):
            new = []
            new.append(currLine[row][column])
            output.append(new)
        column = column + 1
        newline = "\n"
        output.append(newline)

    for row in range(0, len(output)):
        for column in range (0, len(output[row])):
            outputFile.write(str(output[row][column]))

    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()
