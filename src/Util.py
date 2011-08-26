'''
Created on Aug 25, 2011

@author: wildicv
'''

def fileContentsToList(file):
    
    lineList = []
    
    try:
        fileParser = open(file, 'r')
        
    except:
        print "[!] Unable to read file"
        
    for line in fileParser.readlines():
        newLine = line.replace('\n', '')
        lineList.append(newLine)
        
    return lineList