mode = input()
n = input()
n = int(n)
a = input()
a = a.split()
b = input()
b = b.split()
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])
a.sort()
b.sort()
if mode == '2':
    b.reverse()
c=[]
for i in range(n):
    c.append(max(a[i],b[i]))
print(sum(c))
