sd=[[0,4,3,6,9,2,0,8,7],[7,0,0,5,4,8,3,0,2],[5,0,8,0,7,0,4,0,9],[2,6,0,0,3,5,1,7,0],[4,0,5,8,6,7,9,0,0],[0,3,7,2,0,9,6,0,4],[9,8,2,3,5,0,7,4,6],[0,0,4,0,8,6,2,0,1],[6,7,1,9,2,0,8,0,5]]
#sd=[[0, 0, 5, 3, 0, 0, 0, 0, 0],
#    [8, 0, 0, 0, 0, 0, 0, 2, 0],
#    [0, 7, 0, 0, 1, 0, 5, 0, 0],
#    [0, 4, 0, 0, 0, 5, 3, 0, 0],
#    [0, 1, 0, 0, 7, 0, 0, 0, 6],
#    [0, 0, 3, 2, 0, 0, 0, 8, 0],
#    [0, 6, 0, 5, 0, 0, 0, 0, 9],
#    [0, 0, 0, 4, 0, 0, 0, 3, 0],
#    [0, 0, 0, 0, 0, 9, 7, 0, 0]]#定义数独
sdp = dict()#数独的可能数值字典
for i in range(9):
    for j in range(9):
        sdp[i, j] = [[1, 2, 3, 4, 5, 6, 7, 8, 9], list()]
        #每一格的可能性【0】为1到9，相关格子坐标【1】为列表
for r in range(9):
    for c in range(9):
        #每一个格子
        for i in range(9):
            if not (r,i) in sdp[(r, c)][1]:
                sdp[r, c][1].append((r, i))#相关格子坐标列表中加入这一行的所有格子坐标
            if not (i, c) in sdp[(r, c)][1]:
                sdp[r, c][1].append((i, c))#相关格子坐标列表中加入这一列的所有格子坐标
        for i in range((r//3)*3, (r//3)*3+3):
            for j in range((c//3)*3, (c//3)*3+3):
                if not (i, j) in sdp[(r, c)][1]:
                    sdp[r, c][1].append((i, j))#相关格子坐标列表中加入所在小九宫格的所有格子坐标
        sdp[r, c][1].remove((r, c))#相关格子坐标列表中删除自己的坐标


def refreshp(sd=sd,sdp=sdp):
    for r in range(9):
        for c in range(9):
            #每一个格子
            if sd[r][c] != 0:
                sdp[(r, c)][0] = [sd[r][c]]#数独可能性变为数独已确定的数值
            for each in sdp[(r, c)][1]:
                if sd[r][c] in sdp[each][0]:
                    sdp[each][0].remove(sd[r][c])


def fill(sd = sd, sdp = sdp):
    s=0
    for r in range(9):
        for c in range(9):
            if len(sdp[(r,c)][0]) == 1 and sd[r][c] == 0:
                sd[r][c] = sdp[(r,c)][0][0]#将已确认的值填入
                s+=1
    return(s)


while True:
    refreshp()
    a=fill()
    if a==0:
        break

s=1
for r in range(9):
    for c in range(9):
        #每一个格子
        s*=len(sdp[(r, c)][0])#打印可能性的总数
        print(len(sdp[(r, c)][0]),end=" ")
    print()
print(s)