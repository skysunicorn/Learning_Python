def test(sd,r,c):
    horinzontal_test=False
    sample=[0,0,0,0,0,0,0,0,0]
    standard=[1,1,1,1,1,1,1,1,1]
    for j in range(1,10):
        sample[sd[r][j]-1]+=1
    if sample == standard:
        horizontal_test=True
    vertical_test=False
    sample=[0,0,0,0,0,0,0,0,0]
    for i in range(1,10):
        sample[sd[i][c]-1]+=1
    if sample == standard:
        vertical_test=True
    square_test=False
    sample=[0,0,0,0,0,0,0,0,0]
    unitr=(r+2)//3
    unitc=(c+2)//3
    for i in range((unitr-1)*3+1,unitr*3+1):
        for j in range((unitc-1)*3+1,unitc*3+1):
            sample[sd[i][j]-1]+=1
    if sample == standard:
        square_test=True
    return(horizontal_test*vertical_test*square_test)
r1=[0,1,2,3,4,5,6,7,8,9]
r2=[0,4,5,6,7,8,9,1,2,3]
r3=[0,7,8,9,1,2,3,4,5,6]
r4=[0,1,2,3,4,5,6,7,8,9]
r5=[0,4,5,6,7,8,9,1,2,3]
r6=[0,7,8,9,1,2,3,4,5,6]
r7=[0,1,2,3,4,5,6,7,8,9]
r8=[0,4,5,6,7,8,9,1,2,3]
r9=[0,7,8,9,1,2,3,4,5,6]
sd=[[],r1,r2,r3,r4,r5,r6,r7,r8,r9]
