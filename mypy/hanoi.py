import sys
sys.setrecursionlimit(1048576)
times=0
def hanoisolve(n,x="x",y="y",z="z"):
        global times
        if n==1:
                times+=1
                print("step ",times,": ",x, " --> ", z)
        else:
                hanoisolve(n-1, x, z, y)
                times+=1
                print("step ",times,": ",x, " --> ", z)
                hanoisolve(n-1,y,x,z)
hanoilevel=int(input("Set hanoi level:"))
hanoisolve(hanoilevel)
print("total steps: ", times)
