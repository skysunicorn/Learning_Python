#sd=[[],[0,0,4,3,6,9,2,0,8,7],[0,7,0,0,5,4,8,3,0,2],[0,5,0,8,0,7,0,4,0,9],[0,2,6,0,0,3,5,1,7,0],[0,4,0,5,8,6,7,9,0,0],[0,0,3,7,2,0,9,6,0,4],[0,9,8,2,3,5,0,7,4,6],[0,0,0,4,0,8,6,2,0,1],[0,6,7,1,9,2,0,8,0,5]]
#sd=[[],[0,0,4,3,0,0,2,0,8,7],[0,7,0,0,5,4,8,3,0,0],[0,0,0,8,0,7,0,4,0,9],[0,2,6,0,0,3,0,1,0,0],[0,4,0,5,8,0,0,0,0,0],[0,0,3,7,2,0,0,0,0,0],[0,9,8,2,3,5,0,7,4,6],[0,0,0,4,0,8,6,2,0,1],[0,6,7,1,9,2,0,8,0,5]]
#sd=[[],[0,0,0,0,3,0,1,0,0,0],[0,0,1,2,0,0,0,9,3,0],[0,9,8,0,0,0,0,0,6,1],[0,0,0,9,1,7,2,3,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,7,5,6,9,8,0,0],[0,5,9,0,0,0,0,0,7,3],[0,0,6,1,0,0,0,5,4,0],[0,0,0,0,9,0,3,0,0,0]]
#sd=[[],[0,0,8,0,0,0,0,0,0,0],[0,3,5,0,0,0,7,0,0,0],[0,0,0,9,0,0,1,0,0,0],[0,0,0,0,0,0,0,6,4,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,4,0,0,0,0,0,0],[0,0,0,0,3,0,0,5,0,0],[0,0,0,0,9,0,0,0,1,6],[0,0,0,0,0,0,0,0,8,0]]
#sd=[[],[0,0,0,0,0,0,2,0,5,0],[0,0,7,8,0,0,0,3,0,0],[0,0,0,0,0,0,4,0,0,0],[0,5,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,3,0,7,0,8],[0,2,0,0,0,0,0,0,4,0],[0,0,0,0,0,0,5,0,9,0],[0,1,0,0,7,0,0,0,0,0]]
#sd=[[],[0,9,6,1,3,7,2,8,5,4],[0,0,7,8,0,0,0,3,0,0],[0,0,0,0,0,0,4,0,0,0],[0,5,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,3,0,7,0,8],[0,0,0,0,0,0,0,0,4,0],[0,0,0,0,0,0,5,0,9,0],[0,1,0,0,7,0,0,0,0,0]]
#sd=[[],[0,0,0,5,3,0,0,0,0,0],[0,8,0,0,0,0,0,0,2,0],[0,0,7,0,0,1,0,5,0,0],[0,4,0,0,0,0,5,3,0,0],[0,0,1,0,0,7,0,0,0,6],[0,0,0,3,2,0,0,0,8,0],[0,0,6,0,5,0,0,0,0,9],[0,0,0,4,0,0,0,0,3,0],[0,0,0,0,0,0,9,7,0,0]]
if 1:
    sd=[[],
        [-1,    0,0,0,  0,0,0,  0,0,0],
        [-1,    0,0,0,  0,0,0,  0,3,0],
        [-1,    0,0,4,  0,0,0,  9,0,0],

        [-1,    8,0,0,  4,3,7,  0,0,2],
        [-1,    0,4,0,  1,5,8,  0,6,0],
        [-1,    0,0,0,  2,6,9,  0,0,0],

        [-1,    0,0,9,  0,0,0,  4,0,0],
        [-1,    0,7,0,  0,8,0,  0,9,0],
        [-1,    0,0,0,  0,0,0,  0,0,0]]
sdp=[]
step=[['Already certain:']]
sss=[0]
def pop_out(p,sdin=sd,sdpin=sdp):
    num=sdin[p[0]][p[1]]
    for i in range(1,10):
        if num in sdpin[i][p[1]]:
            sdpin[i][p[1]].remove(num)
        if num in sdpin[p[0]][i]:
            sdpin[p[0]][i].remove(num)
    unitr=(p[0]+2)//3
    unitc=(p[1]+2)//3
    for i in range((unitr-1)*3+1,unitr*3+1):
        for j in range((unitc-1)*3+1,unitc*3+1):
            if num in sdpin[i][j]:
                sdpin[i][j].remove(num)
    sdpin[p[0]][p[1]]=[num]
for i in range(10):
    sdp.append([])
    for j in range(10):
        sdp[i].append([1,2,3,4,5,6,7,8,9])
print('original:')
def show(sdin=sd):
    for i in range(1,10):
        for j in range(1,10):
            print(sdin[i][j],end='  ')
        print()
show(sd)
for i in range(1,10):
    for j in range(1,10):
        if sd[i][j]!=0:
            pop_out([i,j])
def certain(sdin=sd,sdpin=sdp):
    goon=True
    while goon==True:
        c=0
        for i in range(1,10):
            for j in range(1,10):
                if len(sdpin[i][j])==1 and sdin[i][j]==0:
                    c+=1
                    sdin[i][j]=sdpin[i][j][0]
                    pop_out([i,j],sdin,sdpin)
                    #print(sdin[i][j],'inserted in','row',i,'column',j)
                    sss[0]+=1
                    step[0].append(str(sdin[i][j])+' inserted in row '+str(i)+' column '+str(j))
        if c==0:
            goon=False
    return(sdin,sdpin)
key=certain()
sd=key[0][:]
sdp=key[1][:]
print('already certain:')
show(sd)
def check(sdp=sdp):
    s=[0,0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        for j in range(1,10):
            s[len(sdp[i][j])]+=1
    return(s)
def guess(sdin=sd,sdpin=sdp):
    cen=check(sdpin)
    if cen[1]<81 and cen[0]==0:
        #print(cen)
        maxn=0
        maxp=[0,0,9]
        for i in range(1,10):
            for j in range(1,10):
                if len(sdpin[i][j])>1:
                    pc=len(sdpin[i][j])
                    bsd = []
                    for ii in range(10):
                        bsd.append([])
                        for jj in range(10):
                            bsd[ii].append([0])
                    for k in range(1,10):
                        if len(sdpin[i][k])>=2:
                            bsd[i][k][0]=1
                            if len(sdpin[i][k])==2 and pc==2:
                                bsd[i][k][0] = 2
                        if len(sdpin[k][j])>=2:
                            bsd[i][k][0]=1
                            if len(sdpin[k][j])==2 and pc==2:
                                bsd[i][k][0] = 2
                    unitr=(i+2)//3
                    unitc=(j+2)//3
                    for k in range((unitr-1)*3+1,unitr*3+1):
                        for l in range((unitc-1)*3+1,unitc*3+1):
                            if len(sdpin[l][k])>=2:
                                bsd[k][l][0]=1
                                if len(sdpin[l][k])==2 and pc==2:
                                    pc=2
                    n=0
                    for k in range(1,10):
                        for l in range(1,10):
                            n=n+sum(bsd[k][l])
                    if n>maxn:
                        maxn=n
                        maxp=[i,j,pc]
                    elif n==maxn and pc<maxp[2]:
                        maxn=n
                        maxp=[i,j,pc]
        if maxp==[0,0,9]:
            for i in range(1,10):
                for j in range(1,10):
                    if len(sdpin[i][j])>=2:
                        maxp=[i,j]
        if maxp!=[0,0,9]:
            tt=len(sdpin[maxp[0]][maxp[1]])-1
        else:
            tt=-1
        turn=-1
        correct=0
        while turn<tt and maxp!=[0,0,9]:
            turn+=1
            sp=sdpin[maxp[0]][maxp[1]][turn]
            #print('supposing row',maxp[0],'column',maxp[1],'is',sp)
            sss[0]+=1
            step.insert(0,['supposing row '+str(maxp[0])+' column '+str(maxp[1])+' is '+str(sp)+' (among'+str(sdpin[maxp[0]][maxp[1]])+')'+' n['+str(turn+1)+'/'+str(tt+1)+']'])
            #print(sdpin[maxp[0]][maxp[1]])
            #print(sdpin[maxp[0]][maxp[1]][turn])
            sdtin=[[]]
            sdptin=[[]]
            for i in range(1,10):
                sdtin.append([0])
                sdptin.append([[0]])
                for j in range(1,10):
                    sdtin[i].append(sdin[i][j])
                    sdptin[i].append([])
                    for k in range(len(sdpin[i][j])):
                        sdptin[i][j].append(sdpin[i][j][k])
            sdtin[maxp[0]][maxp[1]]=sp
            sdptin[maxp[0]][maxp[1]]=[sp]
            pop_out(maxp,sdtin,sdptin)
            #cen = check(sdptin)
            #print(cen)
            certain(sdtin,sdptin)
            key=guess(sdtin,sdptin)
            if key=='fail':
                #print('trial failed')
                sss[0]+=1
                step.pop(0)
            elif key=='succeed':
                correct+=1
                return('succeed')
        return('fail')
    elif cen[0]>0:
        #print('trial failed')
        return('fail')
    else:
        print('done\nSucceeded!!!\nAnswer:')
        show(sdin)
        for i in range(len(step)):
            for j in range(len(step[len(step)-1-i])):
                print(step[len(step)-1-i][j])
            print()
        return('succeed')
guess(sd,sdp)
print('totally',sum(sss),'steps')