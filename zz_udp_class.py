import socket
class ZZUdpClass(object):
    def __init__(self,host,port,timeout):
        self.host =host
        self.port =port
        self.timeout = timeout
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.settimeout(self.timeout)
        self.server.bind((self.host, self.port))
    def rev(self):
        try:
            data,addr= self.server.recvfrom(1024)
            return data,addr
        except socket.timeout:
            print('Time is out. {0} seconds have passed'.format(self.timeout ))
            return False
    def send(self,data,addr):
        try:
            self.server.sendto(data,addr)
        except Exception as err:
            print("error")
            print(err)
            return False