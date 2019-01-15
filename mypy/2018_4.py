n = input()
n = [int(n)]
done = False
d=[0,1,1,1,3,2,6,4,10,7,13]
while not done:
    for i in range(len(n)):
        if n[i] > 10:
            temp = n[i]
            del n[i]
            if temp % 2 == 0:
                n.insert(i,temp - 1)
                n.insert(i,temp - 2)
            else:
                n.insert(i,temp // 2)
                n.insert(i,temp // 2 +1)
            if temp % 3 == 0:
                n.insert(i,1)
        done = True
        for each in n:
            if each > 10:
                done = False
s = 0
for i in range(len(n)):
    if n[i] > 0:
        s+=d[n[i]]
print(s)
