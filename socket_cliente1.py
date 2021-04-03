import socket

mi_socket = socket.socket()
mi_socket.connect(('localhost',8000))

respuesta = mi_socket.recv(1024)
decodrespuesta = respuesta.decode("ascii")
print (respuesta)
a = input()
mi_socket.send(a.encode("ascii"))
respuesta = mi_socket.recv(1024)
decodrespuesta = respuesta.decode("ascii")
print (decodrespuesta)
mi_socket.close()