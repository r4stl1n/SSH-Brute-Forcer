'''
Created on Aug 25, 2011

@author: wildicv
'''
import sys

from threading import Thread
#Check For Paramiko Dependency
try:
    from paramiko import SSHClient
    from paramiko import AutoAddPolicy
except ImportError:
    print 'Missing Paramiko Dependency.'
    sys.exit(0)


class Connection (Thread):
    '''
    This is the class that checks if a specific
    Username and password combination was succesful.
    '''

    def __init__(self,userName, password, targetIp, portNumber, timeoutTime):
        
        super(Connection, self).__init__()
        
        self.userName    = userName
        self.password    = password
        self.targetIp    = targetIp
        self.portNumber  = portNumber
        self.timeoutTime = timeoutTime
        self.status = ""
        
    def run(self):
        
        sshConnection = SSHClient()
        sshConnection.set_missing_host_key_policy(AutoAddPolicy())
        
        try:
            sshConnection.connect(self.targetIp, port = self.portNumber, username = self.userName,
                                  password = self.password, timeout = self.timeoutTime, allow_agent = False,
                                  look_for_keys = False)
            
            self.status = 'ok'
            sshConnection.close()
        except:      
            self.status = 'error'
