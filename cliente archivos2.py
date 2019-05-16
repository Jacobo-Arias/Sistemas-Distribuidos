import xmlrpc.client
import random 
import time

s = xmlrpc.client.ServerProxy('http://localhost:8001')
sesion = True

'''
import getpass
import os
def inicio_sesion():
	Usuario = str(input("Usuario: "))
	Clave = str(getpass.getpass())
	a = s.login(Usuario,Clave)
	print (a)
	return a


def register():
	Usuario = input("Usuario: ")
	Clave = getpass.getpass()
	return s.registro(Usuario,Clave)

def menu1():
	print("1. Login")
	print("2. Register")
	print("0. Salir \n")


while not sesion:
	menu1()
	op2 = int(input())
	if op2 == 1:
		sesion = inicio_sesion()
	elif op2 == 2:
		sesion = register()
	elif op2 == 0:
		break'''


#os.system('cls')
while sesion:
    lista = []
    for i in range (50):
        lista.append(random.randrange(200))
    for i in range(len(lista)):
        lista[i] = str(lista[i])
    lista2 = ''
    for i in lista: 
        lista2 += i + ' '
    f=open('lista.txt','w')
    f.write(lista2)
    f.close()
    print("Esta es su lista de números: ")
    print(lista2)
    time.sleep(0.5)
    print('Ordenando números')
    with open ("lista.txt","rb") as handle:
        binary_data = xmlrpc.client.Binary(handle.read())
        s.server_receive_file(binary_data)
    with open("lista_ordenada.txt", "wb") as handle:
        handle.write(s.enviar().data)
    f = open('lista_ordenada.txt','r')
    a = f.read()
    print('Esta es la lista ordenada:')
    time.sleep(0.3)
    print(a)
    print('Fin')
    time.sleep(1)
    sesion = False