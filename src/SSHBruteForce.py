'''
Created on Aug 25, 2011

@author: wildicv
'''

import sys
from optparse import OptionError
from optparse import OptionParser

#Import the Util Class
from Util import *
#Import the connection class
from Connection import Connection

class SSHBruteForce():

    def __init__(self):
        
        self.info = "Simple SSH Brute Forcer: By Wildicv"
        self.targetIp = ""
        self.userNameList = []
        self.passwordList = []
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
        self.userNameList = fileContentsToList(options.userList)
        self.passwordList = fileContentsToList(options.passwordlist)
        self.verbose = options.verbose
        
    def showStartInfo(self):
        print "[*] %s " % self.info
        print "[*] Brute Forcing %s"     % self.targetIp
        print "[*] Loaded %s Usernames"  % str(len(self.userNameList))
        print "[*] Loaded %s Passwords"  % str(len(self.passwordList))
        print "[*] Brute Force Starting"

    
        