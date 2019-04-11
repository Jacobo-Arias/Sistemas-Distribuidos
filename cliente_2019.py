import xmlrpc.client
import getpass

s = xmlrpc.client.ServerProxy('http://localhost:8001')
sesion = False

def menu2():
	print("1. Suma")
	print("2. Resta")
	print("3. Multiplicacion")
	print("4. Division")
	print("5. Modulo")
	print("0. Salir \n")

def inicio_sesion:
	Usuario = input("Usuario: ")
	Clave = getpass.getpass()
	return s.login(Usuario,Clave)


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
	op = int(input())
	if op == 1:
		sesion = inicio_sesion()
	elif op == 2:
		sesion = register()
	elif op == 0:
		break


while sesion:
	menu2()
	op = int(input("Digite opcion: "))
	a = int(input("Primer numero: "))
	b = int(input("Segundo numero: "))
	if op == 1:
		print("la suma es: " + str(s.suma(a,b)))
	elif op == 3:
		print("la suma es: " + str(s.resta(a,b)))
	elif op == 4:
		print("la suma es: " + str(s.mult(a,b)))
	elif op == 5:
		print("la suma es: " + str(s.div(a,b)))
	elif op == 0:
		break


a =int(input('Ingrese el primer numero: '))
b=int(input('Ingrese el segundo numero: '))
print("la suma es: " + str(s.resta(a,b)))
