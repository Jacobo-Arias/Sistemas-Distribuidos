import socket
import time


mi_socket = socket.socket()
mi_socket.bind(('localhost',8000))
mi_socket.listen(1)



conexion, addr = mi_socket.accept()
print('Nueva conexion establecida')
print (addr)

conexion.send("Digame su nombre")
peticion = conexion.recv(1024)
hora = time.strftime("%X")
fecha = time.strftime("%x")
envio = 'Hola '+ str(peticion)+' usted ha ingresado el '+str(fecha)+' a las '+str(hora)
conexion.send(envio)

conexion.close()
mi_socket.close()