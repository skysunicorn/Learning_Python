nb=""
nb=input("Input number:")
while nb!="end" and nb!="no" and nb!="over" and nb!="ok":
    a=[]
    a.extend(nb)
    n=len(a)
    s=0
    for i in range(n):
        if (i+1)%2==0:
            ss=int(a[i])
            s+=ss
            print(ss,"+",end=" ")
        elif (i+1)%2==1:
            ss=2*int(a[i])
            if ss>=10:
                s+=ss%10+1
                print("1","+",ss%10,"+",end=" ")
            else:
                s+=ss
                print(ss,"+",end=" ")
    print("=",s)
    nb=input("Input number:")
