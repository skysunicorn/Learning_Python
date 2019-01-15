import easygui
lvr=int(input("Level of row="))
lvc=int(input("Level of column="))
matrix=[[-1 for i in range(lvc+2)] for i in range(lvr+2)]
for i in range(1,lvr+1):
    for j in range(1,lvc+1):
        matrix[i][j]=0
num=1
r=1
c=1
direct=0
while num<=lvr*lvc:
    matrix[r][c]=num
    num+=1
    if (matrix[r-1][c+1]!=0) and (matrix[r+1][c-1]!=0):
        if (matrix[r+1][c]==0) and (matrix[r][c+1]==0):
            if direct%2==0:
                c+=1
            elif direct%2==1:
                r+=1
            direct+=1
        elif matrix[r+1][c]==0:
            r+=1
            direct+=1
        elif matrix[r][c+1]==0:
            c+=1
            direct+=1
    elif matrix[r-1][c+1]==0:
        r-=1
        c+=1
    elif matrix[r+1][c-1]==0:
        r+=1
        c-=1
for i in range(1,lvr+1):
    for j in range(1,lvc+1):
        print('%5.0f' % matrix[i][j],end="")
    print()
    print()
