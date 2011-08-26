'''
Created on Aug 25, 2011

@author: wildicv
'''
from threading import Thread
from paramiko import SSHClient
from paramiko import AutoAddPolicy

class Connection (Thread):
    '''
    This is the class that checks if a specific
    Username and password combination was succesful.
    '''

    def __init__(self,userName, passWord, targetIP, portNumber, timeoutTime):
        
        super(Connection, self).__init__()
        
        self.userName    = userName
        self.passWord    = passWord
        self.targetIP    = targetIP
        self.portNumber  = portNumber
        self.timeoutTime = timeoutTime
        self.status = ""
        
    def run(self):
        
        sshConnection = SSHClient()
        sshConnection.set_missing_host_key_policy(AutoAddPolicy())
        
        try:
            sshConnection.connect(self.targetIP, port = self.portNumber, username = self.userName,
                                  password = self.password, pkey = None, timeout = self.timeoutTime,
                                  allow_agent = False, look_for_keys = False)
            
            self.status = 'ok'
            sshConnection.close()
        except:      
            self.status = 'error'
