import socket
import time


mi_socket = socket.socket()
mi_socket.bind(('localhost',8000))
mi_socket.listen(1)



conexion, addr = mi_socket.accept()
print('Nueva conexion establecida')
print (addr)
solinombre = "Digame su nombre"
conexion.send(solinombre.encode("ascii"))
peticion = conexion.recv(1024)
decodpeticion = peticion.decode("ascii")
hora = time.strftime("%X")
fecha = time.strftime("%x")
envio = 'Hola '+ str(decodpeticion)+' usted ha ingresado el '+str(fecha)+' a las '+str(hora)
conexion.send(envio.encode("ascii"))

conexion.close()
mi_socket.close()