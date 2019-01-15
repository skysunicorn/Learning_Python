#r=input('input the range (a whole number greater than 1): ')
import time as t
st=t.time()
r=200000
p=[]
for i in range(2,int(r)+1):
    n=0
    j=2
    while n==0 and j<=(i**(1/2)):
        if i % j == 0:
            n=1
        j+=1
    if n==0:
        p.append(i)
#for each in p:
    #print(each)
print('totally',len(p),'prime numbers')
et=t.time()
print('time used:',et-st,'s')