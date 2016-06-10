#!/usr/bin/python

import sys

def main():
    inputFile = open(sys.argv[1], 'r')
    outputFile = open('outfile', 'w')
    output = [] #To be written to file. Is an 2D array of char

    #Read the whole file. Arrange it as a 2D array with a new row every time
    # newline is reached


    everyLine = inputFile.readlines() # Array containing everyline in the file

    longest = len(everyLine)

    for row in range(0,len(everyLine)):
        if longest < len(everyLine[row]):
            longest = len(everyLine[row])

    #Make square matrix full of white space
    # Note, it uses pass by reference when appending so a new row needs to be made instead of using the same one.
    for row in range(0,longest):
        new = []
        for column in range(0, longest-1):
            new.append(" ")
        new.append("\n")
        output.append(new)

    for row in range (0, len(everyLine)):
        for column in range (0, len(everyLine[row])-1 ):
            output[column][row] = everyLine[row][column]

    for row in range(0,longest-1):
        for column in range(0,longest):
            outputFile.write(output[row][column])







    # # If length of individual line is shorter then count add spaces and
    # # continue. Each time a longer string is reached store its size
    # for line in range (0, len(everyLine)-1): #go through every line
    #     numSpaces = 0
    #     for index in range (0, len(everyLine[line])): #go thru every char in line
    #         if (len(everyLine[line]) > len(everyLine[line-1])-numSpaces):
    #             numSpaces += 1
    #             output.append(" ")
    #         else:
    #             output.append(everyLine[index][line])
    #     output.append("\n")
    # print output
    #
    #
    # # column = 0
    # # columnLength = len(currLine[column]) - 1 # Length of columns in a line
    # # output = []
    # # while (column <= columnLength):
    # #     for row in range(0,len(currLine)):
    # #         print "Row Length:" + str(len(currLine))
    # #         new = []
    # #         new.append(currLine[row][column])
    # #         output.append(new)
    # #     column = column + 1
    # #     newline = "\n"
    # #     output.append(newline)
    #

    inputFile.close()
    outputFile.close()

if __name__ == "__main__":
    main()
