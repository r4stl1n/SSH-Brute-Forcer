'''
Created on Aug 25, 2011

@author: wildicv
'''

def fileContentsToList(fileName):
    
    lineList = []
    
    try:
        fileParser = open(fileName, 'r')
        
    except IOError:
        print "[!] Could not open file %s " % fileName
        
    except:
        print "[!] Could not access file %s" % fileName
        
    for line in fileParser.readlines():
        newLine = line.replace('\n', '')
        lineList.append(newLine)
        
    return lineList

def fileContentsToTuple(fileName):
    
    tupleList = []
    
    try:
        fileParser = open(fileName, 'r')
        
    except IOError:
        print "[!] Could not open file %s " % fileName
        
    except:
        print "[!] Could not access file %s" % fileName
        
    for line in fileParser.readlines():
        newLine = line.replace('\n', '')
        newTuple = (newLine[:line.find(':')],newLine[line.find(':')+1:])
        tupleList.append(newTuple)
        
    return tupleList