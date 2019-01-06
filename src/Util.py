'''
Created on Aug 25, 2011

@author: r4stl1n
'''


def fileContentsToList(fileName):
    lineList = []

    try:
        fileParser = open(fileName, 'r', encoding='latin-1')

    except IOError:
        print("[!] Could not open file " + fileName)

    except:
        print("[!] Could not access file " + fileName)

    for line in fileParser.readlines():
        newLine = line.replace('\n', '')
        lineList.append(newLine)

    return lineList


def fileContentsToTuple(fileName):
    tupleList = []

    try:
        fileParser = open(fileName, 'r')

    except IOError:
        print("[!] Could not open file " + fileName)

    except:
        print("[!] Could not access file " + fileName)

    for line in fileParser.readlines():
        newLine = line.replace('\n', '')
        newTuple = (newLine[:line.find(':')], newLine[line.find(':') + 1:])
        tupleList.append(newTuple)

    return tupleList


def appendLineToFile(line, filename):
    fileHandler = open(filename, "a+")
    fileHandler.write(line + "\n")
    fileHandler.close()
