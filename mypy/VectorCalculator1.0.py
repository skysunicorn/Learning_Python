import easygui as eg
import physics4u as phy4
eg.msgbox("Thank you for choosing Vector Calculator\nPlease input the value as instructed to avoid unexpected error\nClick [Continue] to start","Vector Calculator","Continue")
anotherloop=1
while anotherloop==1:
    msg="Please select the mode you want"
    title="Mode selecting"
    modes=["Total Vector","Force Resolution"]
    confirm=0
    while confirm==0:
        sdmode=eg.choicebox(msg,title,modes)
        msg="Are you sure to choose "+sdmode+"?"
        confirm=eg.boolbox(msg=msg,title="Confirm your choice",choices=("Yes","No"),image=None)
    mulcho=[]
    mulchof=[]
    nvct=int(eg.enterbox(msg="Number of Vectors",title="",default="",strip=True,image=None,root=None))
    for i in range(1,nvct+1):
        magn="Magnitude"+str(i)+"="
        mulcho.append(magn)
        mulchof.append("")
        dire="Direction"+str(i)+"="
        mulcho.append(dire)
        mulchof.append("")
    dpunpw=eg.multenterbox(msg="Please fill in as instructed",title="Input Vectors",fields=mulcho,values=mulchof)
    dp=[]
    for i in range(nvct):
        inpdis=float(dpunpw[2*i])
        drct=phy4.drctpw(dpunpw[2*i+1])
        inpdir1=drct[0]
        inpdeg=drct[1]
        inpdir2=drct[2]
        dp.append((inpdis,inpdir1,inpdeg,inpdir2))
    if sdmode=="Total Vector":
        anmsg=phy4.soltv(dp,fopd='N',wtp=False)
    elif sdmode=="Force Resolution":
        anmsg=phy4.solrf(dp,wtp=False)
    anotherloop=eg.boolbox(msg=anmsg,title="Result",choices=("Run Another Turn","Exit Program"),image=None)
        
