def dsmn(n,a): #--------精确到小数点后n位
    import math
    a=a*(10**n)
    if a%1>=0.5:
        a=math.ceil(a)/(10**n)
    else:
        a=math.floor(a)/(10**n)
    return(a)
def parasov(a,b,c): #----------解二次方程
    dt=b**2-4*a*c
    if dt > 0:
        roots=[(-b+dt**(1/2))/(2*a),(-b-dt**(1/2))/(2*a)]
        print ("x1 = ",roots[0])
        print ("x2 = ",roots[1])
        return(roots)
    elif dt == 0:
        roots=[(-b+dt**(1/2))/(2*a),(-b-dt**(1/2))/(2*a)]
        print ("x1 = x2 = ",roots[0])
        return(roots)
    elif dt < 0:
        roots=[(-b+dt**(1/2))/(2*a),(-b-dt**(1/2))/(2*a)]
        print ("Be Careful! This function has no real roots!")
        print ("x1 = ",roots[0])
        print ("x2 = ",roots[1])
        return(roots)
    else:
        print("Are You Kidding Me???")
def uccal(n1,op,n2):
    import math
    if op=="+":
        result=[]
        result.append(dsmn(4,n1[0]+n2[0]))
        result.append(dsmn(4,math.sqrt((n1[1]**2)+(n2[1]**2))))
        return(result)
    elif op=="*":
        result=[]
        result.append(dsmn(4,n1[0]*n2[0]))
        result.append(dsmn(4,result[0]*math.sqrt(((n1[1]/n1[0])**2)+((n2[1]/n2[0])**2))))
        return(result)
def drctpw(unpw): #---------------------东西南北方向转化给程序
    if unpw=="N" or unpw=="n":
        return(["E",90,"N"])
    elif unpw=="S" or unpw=="s":
        return(["E",90,"S"])
    elif unpw=="W" or unpw=="w":
        return(["W",0,"N"])
    elif unpw=="E" or unpw=="e":
        return(["E",0,"N"])
    else:
        lenun=len(unpw)
        drct1=unpw[0:1]
        drct2=unpw[lenun-1:lenun]
        deg=unpw[1:lenun-1]
        if (drct1=="W") or (drct1=="w") or (drct1=="E") or (drct1=="e"):
            return(drct1,float(deg),drct2)
        else:
            return(drct2,90-float(deg),drct1)
def drcthw(unhw): #-----------------------------东西南北方向转化给人
    if unhw[0]==0:
        del unhw[1:4]
        unhw.append("No direction")
    elif unhw[2]==0:
        del unhw[2:4]
    elif unhw[2]==90:
        del unhw[1:3]
    return(unhw)
def coslaw(b,A,c):#------------余弦定理
    import math
    A=A/180*math.pi
    a=math.sqrt(b**2+c**2-2*b*c*math.cos(A))
    a=dsmn(4,a)
    print("a=",a)
    B=math.asin(b*math.sin(A)/a)/math.pi*180
    B=dsmn(4,B)
    print("B=",B)
    print("C=",180-A-B)
def solvector(dp):
    import math
    if type(dp)==int:
        dpn=dp
        dp=[]
        for i in range(dpn):
            inpdis=float(input("Magnitude="))
            drct=drctpw(input("Direction:"))
            inpdir1=drct[0]
            inpdeg=drct[1]
            inpdir2=drct[2]
            dp.append((inpdis,inpdir1,inpdeg,inpdir2))
    lenod=len(dp)
    dish=0
    disv=0
    for runt in range(lenod):
        if dp[runt][1]=="W" or dp[runt][1]=="w":
            dish+=-dp[runt][0]*math.cos(dp[runt][2]/180*math.pi)
        elif dp[runt][1]=="E" or dp[runt][1]=="e":
            dish+=dp[runt][0]*math.cos(dp[runt][2]/180*math.pi)
        else:
            print("INPUT ERROR")
            break
        if dp[runt][3]=="S" or dp[runt][3]=="s":
            disv+=-dp[runt][0]*math.sin(dp[runt][2]/180*math.pi)
        elif dp[runt][3]=="N" or dp[runt][3]=="n":
            disv+=dp[runt][0]*math.sin(dp[runt][2]/180*math.pi)
        else:
            print("INPUT ERROR")
            break
    d1=""
    deg=0
    d2=""
    if dish>=0:
        d1="E"
    else:
        d1="W"
    if disv>=0:
        d2="N"
    else:
        d2="S"
    return(dish,d1,disv,d2)
def solrf(dp=1,wtp=True):
    import math
    keyr=solvector(dp)
    dish=keyr[0]
    d1=keyr[1]
    disv=keyr[2]
    d2=keyr[3]
    dish=dsmn(4,dish)
    disv=dsmn(4,disv)
    if wtp==True:
        print("Horizontal Part= ",dish,"unit [",d1,"]")
        print("Vertical   Part= ",disv,"unit [",d2,"]")
        answerpw1=[dish]+drctpw(d1)
        answerpw2=[disv]+drctpw(d2)
        return([answerpw1,answerpw2])
    else:
        anmsg="Horizontal Part= "+str(dish)+"unit ["+d1+"]\n"
        anmsg=anmsg+"Vertical   Part= "+str(disv)+"unit ["+d2+"]"
        return(anmsg)
def soltv(dp,fopd="EW",wtp=True):#------------向量加减
    import math
    import easygui as eg
    import sys
    keyr=solvector(dp)
    dish=keyr[0]
    d1=keyr[1]
    disv=keyr[2]
    d2=keyr[3]
    if dish!=0:
        deg=math.atan(abs(disv)/abs(dish))/math.pi*180
    else:
        deg=90
    deg=dsmn(4,deg)
    dist=math.sqrt((dish**2)+(disv**2))
    dist=dsmn(4,dist)
    answerpw=[dist,d1,deg,d2]
    answerhw=[dist,d1,deg,d2]
    drcthw(answerhw)
    if (fopd=="EW") or (fopd=="WE") or (fopd=="ew") or (fopd=="we") or (fopd=="E") or (fopd=="W") or (fopd=="e") or (fopd=="w"):
        doph=1
    elif (fopd=="SN") or (fopd=="NS") or (fopd=="sn") or (fopd=="ns") or (fopd=="S") or (fopd=="N") or (fopd=="s") or (fopd=="n"):
        doph=2
    if len(answerhw)==4 and wtp==True:
        if doph==1:
            print("Total Vector= ",answerhw[0],"unit [",answerhw[1]," ",answerhw[2],"˚ ",answerhw[3],"]")
        elif doph==2:
            print("Total Vector= ",answerhw[0],"unit [",answerhw[3]," ",90-answerhw[2],"˚ ",answerhw[1],"]")
    elif len(answerhw)==2 and wtp==True:
        print("Total Vector= ",answerhw[0],"unit [",answerhw[1],"]")
    elif len(answerhw)==4 and wtp==False:
        if doph==1:
            anmsg="Total Vector= "+str(answerhw[0])+"unit ["+answerhw[1]+" "+str(answerhw[2])+"˚ "+answerhw[3]+"]"
        elif doph==2:
            anmsg="Total Vector= "+str(answerhw[0])+"unit ["+answerhw[3]+" "+str(90-answerhw[2])+"˚ "+answerhw[1]+"]"
    elif len(answerhw)==2 and wtp==False:
        anmsg="Total Vector= "+str(answerhw[0])+"unit ["+answerhw[1]+"]"
    if wtp==True:
        return(answerpw)
    else:
        return(anmsg)

        
