__author__ = 'touko'
# -*- coding: utf-8 -*-
#!/usr/bin/python


def blockFunc( portNumber1, portNumber2, domainName ):
    portNumber1 = str(portNumber1)
    portNumber2 = str(portNumber2)
    listAdd('frontend ss-in-' +portNumber1)
    listAdd('        bind *:' +portNumber1)
    listAdd('        default_backend ss-out-' +portNumber1)
    listAdd('backend ss-out-' +portNumber1)
    listAdd('        server server1 ' +domainName+ ':' +portNumber2+ ' maxconn 20480')
    listAdd(' ')
    #return sStr

def listAdd( sStr ):
    blockList.append(sStr)
    return sStr


#values
blockList = []
targetDomainName = raw_input("Enter your target domain: ")
listenPortStart = raw_input("Enter your first listening port: ")
forwardPortStart = raw_input("Enter your first forwarding port: ")
numbers = raw_input("Enter your port numbers: ")
#values end

defaultStr = '''global
        ulimit-n  51200
defaults
        log global
        mode    tcp
        option  dontlognull
        timeout connect 1000
        timeout client  150000
        timeout server 150000
        '''

listAdd(defaultStr)

for i in range(0, int(numbers) ):
    blockFunc( int(listenPortStart) + i, int(forwardPortStart) + i, targetDomainName )

outputStr = '\n'.join(blockList)
print outputStr

outputFileName = raw_input("save file name [default : haproxy.cfg]: ")
if outputFileName == '' :
    outputFileName = 'haproxy.cfg'

fi = open( outputFileName, 'w')
fi.write( outputStr )
fi.close( )
