'''
Created on Jul 27, 2013

@author: chuck
'''

import socket
import socks
import httplib

def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket
    
def main():
    connectTor()
    conn = httplib.HTTPConnection("google.com")
    response = conn.getresponse()
    print(response.read())
    
if __name__ == "__main__":
    main()