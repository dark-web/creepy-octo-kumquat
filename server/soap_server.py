from twisted.web import soap, resource, server

import os

class SOAPServer(soap.SOAPPublisher):

    def soap_listdir(self, direc):
        print "Got: ", direc
        ret = []
        for i in range(0, 10):
            ret.append(direc + ' ' + str(i))
        return ret

def main():
    from twisted.internet import reactor
    root = resource.Resource()
    root.putChild('SOAP', SOAPServer())
    reactor.listenTCP(8443, server.Site(root))
    reactor.run()

if __name__ == '__main__':
    main()
