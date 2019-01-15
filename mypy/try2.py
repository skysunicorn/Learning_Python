lv = int(input("Set Level:"))
pt = [[0 in range(lv + 1)] in range(lv + 1)]
print(pt)
for i in range(1, lv + 1):
    for j in range(1, lv + 1):
        pt[i][1] = 1
        pt[1][j] = 1
for i in range(1, lv + 1):
    for j in range(1, i + 1):
        print(pt[i + 1 - j][j], end="  ")
    print()
list()
