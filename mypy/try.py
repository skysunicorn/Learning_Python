import timeit as ti
t=ti.repeat('y=2*x+1','x=1',repeat=100)
print(min(t))