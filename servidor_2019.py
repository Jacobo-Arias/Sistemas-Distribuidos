from xmlrpc.server import SimpleXMLRPCServer
users = [["jacobo","admin"]]


class operaciones:
	def login(self,a,b):
		c = [a,b]
		if a in users

	def registro


	def	suma(self,a,b):
		return a+b

	def	resta(serlf,a,b):
		return a-b

	def	mult(serlf,a,b):
		return a*b

	def	div(serlf,a,b):
		return a/b


server = SimpleXMLRPCServer(("localhost", 8001))
server.register_instance(operaciones())
print ("Hola amigos, soy el servidor implementado con clases")
server.serve_forever()
