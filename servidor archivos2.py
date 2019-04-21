from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
#import os
users = [['jacobo', 'admin']]


class archivos():
    
    def ordenamiento(self):
        f = open('lista.txt','r')
        a = f.read()
        f.close()
        a = a.split()
        for i in range(len(a)):
            a[i] = int(a[i])
        print(a)
        a.sort()
        lista2 = ''
        for i in a: 
            lista2 += str(i) + ' '
        f = open('lista.txt','w')
        f.write(lista2)
        f.close()
        return True
    
    def server_receive_file(self,arg):
        with open("lista.txt", "wb") as handle: 
            handle.write(arg.data)
        self.ordenamiento()
        return True
        
    
    def enviar(self):
        with open("lista.txt", "rb") as handle:
            return xmlrpc.client.Binary(handle.read())

    
'''def login(self,a,b):
        c = [a,b]
        if c in users:
            return True
        else:
            return False

    def registro(self,a,b):
        users.append([a,b])'''




server = SimpleXMLRPCServer(("localhost", 8001))
server.register_instance(archivos())
print ("Hola amigos, soy el servidor ordenador que elementos de un archivo")
server.serve_forever()