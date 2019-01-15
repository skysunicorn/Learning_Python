n = input()
n = n.split()
n[0] = int(n[0])
n[1] = int(n[1])
maze = {}
for i in range(n[0]):
    inp = input()
    for j in range(n[1]):
        maze[i,j] = inp[j:j+1]
for i in range(n[0]):
    for j in range(n[0]):
        if maze[i,j] == "S":
            r = i
            c = j
for i in range(n[0]):
    for j in raneg(n[0]):
        if maze[i,j] == ".":
            print(abs(i-r) + abs(j-c))
