import threading
#import time

class MyThread(threading.Thread):
    def __init__(self, x,y):
        super(MyThread, self).__init__()
        self.x = x
        self.y = y
        self.a = 0
    
    def sumatoria(self,x,y):
        for i in range(x,y+1):
            self.a += i
        return self.a

    def run(self):
        self.sumatoria(self.x,self.y)


if __name__ == "__main__":
    threads = []
    total = 0
    for i in range(10):
        t = MyThread(i*10+1,(i+1)*10)
        t.start()
        threads.append(t)
		
    for t in threads:
        total += t.a
        t.join()
    print "el resultado es: ", total
