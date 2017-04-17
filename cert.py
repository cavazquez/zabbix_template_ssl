import ssl
import datetime
import time
import socket
from io import StringIO

class Cert:

    def __init__(self,cert):
        self._issuer = dict(x[0] for x in cert['issuer'])
        self._subject = dict(x[0] for x in cert['subject'])
        self._notAfter = cert['notAfter']
        self._notBefore = cert['notBefore']
        self._serialNumber = cert['serialNumber']
        self._subjectAltName = dict(x for x in cert['subjectAltName'])
        self._version = cert['version']


    def __str__(self):
        s = StringIO('')

        s.write('Issuer:\n')
        for x in self._issuer:
            s.write(' {} : {}\n'.format(x,self._issuer[x]))

        s.write('Subject:\n')
        for x in self._subject:
            s.write(' {} : {}\n'.format(x,self._subject[x]))

        cert_time_notAfter = datetime.datetime.utcfromtimestamp(ssl.cert_time_to_seconds(self._notAfter))
        cert_time_notBefore = datetime.datetime.utcfromtimestamp(ssl.cert_time_to_seconds(self._notBefore))
        now = datetime.datetime.now()
        cert_time_days_notAfter = (cert_time_notAfter - now).days
        cert_time_days_notBefore = (cert_time_notBefore - now).days

        s.write('notAfter : {}\n'.format( cert_time_days_notAfter ))
        s.write('notBefore : {}\n'.format( cert_time_days_notBefore ))

        s.write('Serial : {}\n'.format(self._serialNumber))

        s.write('subjectAltName:\n')
        for x in self._subjectAltName:
            s.write(' {} : {}\n'.format(x,self._subjectAltName[x]))

        s.write('Version : {}'.format(self._version))
        return s.getvalue()

context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(socket.AF_INET),
        server_hostname="*.dc.uba.ar")

# Connect to host
conn.connect(("www.dc.uba.ar",443))

# Get certificate
cert = conn.getpeercert()

print(Cert(cert))


