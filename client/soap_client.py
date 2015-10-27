from twisted.web.soap import Proxy

from twisted.internet import reactor

def printResult(value):
    print repr(value)
    reactor.stop()

def printError(error):
    print 'Error', error
    reactor.stop()

proxy = Proxy('http://localhost:8443/SOAP')
proxy.callRemote('listdir', 'User').addCallbacks(printResult, printError)
reactor.run()