'''
Created on Aug 25, 2011

@author: wildicv
'''

def fileContentsToList(file):
    
    lineList = []
    
    try:
        fileParser = open(file, 'r')
        
    except IOError:
        print "[!] Could not open file %s " % file
        
    except:
        print "[!] Could not access file %s" % file
        
    for line in fileParser.readlines():
        newLine = line.replace('\n', '')
        lineList.append(newLine)
        
    return lineList