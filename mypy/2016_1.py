a = input()
b = input()
a = list(a)
b = list(b)
k = True
if len(a) != len(b):
    k=False
else:
    for i in range(len(b)):
        if b[i] == '*':
            continue
        elif b[i] in a:
            a.remove(b[i])
        else:
            k=False
    if k == True:
        print('A')
    else:
        print('N')
