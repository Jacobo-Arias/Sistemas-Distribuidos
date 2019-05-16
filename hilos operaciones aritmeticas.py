import threading
import time

class MyThread(threading.Thread):
    def __init__(self,x,y,op):
            super(MyThread, self).__init__()
        self.num1 = x
        self.num2 = y
        self.op = op
        self.valor = 0

	def suma(self, a,b):
        return a+b
    
    def resta(self, a,b):
        return a-b

    def Division(self, a,b):
		return a/b
    
    def Multiplicacion(self, a,b):
		return a*b

 	def run(self):
        if op == 1: self.valor = self.suma(self.num1,self.num2)
        elif op == 2: self.valor = self.resta(self.num1,self.num2)
        elif op == 3: self.valor = self.Division(self.num1,self.num2)
        elif op == 4: self.valor = self.Multiplicacion(self.num1,self.num2)
        return self.valor
 	    


if __name__ == "__main__":
    threads = []
    n=input('amiguito ingresa el primer numero: ')  
    m=input('amiguito ingresa el segundo numero: ')
    for i in range(4):
        t = MyThread(n,m,i)
        t.start()
        threads.append(t)
    resultados=['suma','resta','division','multiplicacion']
    i = 0
    for t in threads:
        print "el resultado de la ",resultados[i],'es: ',t.valor
        i +=1
        t.join()
    
