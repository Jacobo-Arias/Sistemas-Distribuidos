import time
import random
import os

vecs = [[],[],[]]


while True:
    
    vecs[0].append(random.randrange(1000))
    vecs[1].append(random.randrange(1000))
    vecs[2].append(random.randrange(1000))
    print('\n\n')      
    print ('a: ',vecs[0])
    print ('b: ',vecs[1])
    print ('c: ',vecs[2])
    time.sleep(0.5)
    aux = random.randrange(0,1000)
    if (aux<300):
        n1 = random.randrange(3)
        n2 = random.randrange(3)
        while n1==n2:
            n2 = random.randrange(3)
        print('-------------------------------------------------------------\n\n\n')
        print(vecs[n1],'  ->  ',vecs[n1][-1])
        print(vecs[n2],'  ->  ',vecs[n2][-1],'\n')
        if vecs[n1][-1] >= vecs[n2][-1]:
            vecs[n2][-1] = vecs[n1][-1] + 1
            print(vecs[n1],'  ->  ',vecs[n1][-1])
            print(vecs[n2],'  ->  ',vecs[n2][-1])
            print('\n\n\n ------------------------------------------------------------')
            time.sleep(3)
        else: 
            print('\n\n\n ------------------------------------------------------------')

        time.sleep(3)
        

        



    
