import xmlrpc.client
import getpass
import os

s = xmlrpc.client.ServerProxy('http://localhost:8001')
sesion = False

def menu2():
	print("1. Suma")
	print("2. Resta")
	print("3. Multiplicacion")
	print("4. Division")
	print("0. Salir \n")

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
		break

os.system('cls')
while sesion:
	menu2()
	op = int(input("Digite opcion: "))
	os.system('cls')
	if op == 0:
		break
	a = int(input("Primer numero: "))
	b = int(input("Segundo numero: "))
	if op == 1:
		print("la suma es: " + str(s.suma(a,b)))
	elif op == 2:
		print("la resta es: " + str(s.resta(a,b)))
	elif op == 3:
		print("la multiplicacion es: " + str(s.mult(a,b)))
	elif op == 4:
		print("la division es: " + str(s.div(a,b)))
