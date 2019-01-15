n = "8 5"
pho = "0 6 4 3 7"
inp = ["0 1","0 2","2 3","4 3","6 1","1 5","7 3"]
n = n.split()
pho = pho.split()
m = int(n[1])
n = int(n[0])
for i in range(len(pho)):
    pho[i] = int(pho[i])
h = []
for  i in range(n):
    h.append([])
for i in range(n-1):
    r = inp[i]
    r = r.split()
    r[0] = int(r[0])
    r[1] = int(r[1])
    h[r[0]].append(r[1])
    h[r[1]].append(r[0])
print(h)
l = dict()
for i in range(len(pho)):
    for j in range(i+1,len(pho)):
        d = 1
        done = False
        to = []
        to = h[pho[i]]
        print("finding",pho[i],"to",pho[j])
        print("distance =",d)
        print(to)
        if h[pho[j]] in to:
            done = True
        else:
            print(h[pho[j]],"not in",to)
        while not done:
            d+=1
            print("distance =",d)
            too = to[:]
            for k in range(len(too)):
                to.extend(h[too[k]])
            to = set(to)
            to = list(to)
            print(to)
            if h[pho[j]][0] in to:
                done = True
                break
            else:
                print(h[pho[j]],"not in",to)
        l[pho[i],pho[j]] = d
print(l)
