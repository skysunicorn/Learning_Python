n = input()
n = int(n)
f = {}
for i in range(n):
    inp = input()
    inp = inp.split()
    for j in range(n):
        p = int(inp[j])
        f[i,j] = p
def check(f,n):
    for i in range(n):
        r = []
        c = []
        for j in range(n):
            r.append(f[i,j])
            c.append(f[j,i])
        if r != sorted(r) or c != sorted(c):
            return(False)
    return(True)
def turn(f,n):
    ff = {}
    for i in range(n):
        for j in range(n):
            ff[j,n-1-i] = f[i,j]
    return(ff)
for k in range(4):
    if check(f,n):
        for i in range(n):
            for j in range(n):
                print(f[i,j],end=" ")
            print()
        break
    else:
        f = turn(f,n)
