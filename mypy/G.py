n = int(input())
a = input()
b = input()
a = list(a)
b = list(b)
s=0
for i in range(n):
    if a[i] == b[i]:
        s+=1
print(s)
