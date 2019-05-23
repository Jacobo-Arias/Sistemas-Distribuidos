import socket

mi_socket = socket.socket()
mi_socket.connect(('localhost',8000))

respuesta = mi_socket.recv(1024)
print (respuesta)
a = raw_input()
mi_socket.send(a)
respuesta = mi_socket.recv(1024)
print (respuesta)
mi_socket.close()