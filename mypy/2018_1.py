n = input()
n = int(n)
v = []
for i in range(n):
    s = input()
    s = float(s)
    v.append(s)
v.sort()
l = len(v)
r = []
for i in range(1,l):
    r.append(v[i]-v[i-1])
l = len(r)
nei = []
for i in range(l):
    nei.append(r[i] / 2)
    nei.append(r[i] / 2)
del nei[0]
del nei[-1]
l = len(nei)
a = []
for i in range(int(l / 2)):
    a.append(nei[2*i] + nei[2*i+1])
mini = min(a)
print(mini)
