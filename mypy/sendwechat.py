#coding=utf8
import itchat as c
import easygui as g
import random 
txtcho=[]
txtcho.append("[ELSE:input text]")
txtcho.append("hello？、在吗？")
txtcho.append("thx")
txtcho.append("WOW!")
txtcho.append("[ 3 random 哈哈哈哈]")
txtcho.append("[END send no more]")
login=g.boolbox("BE CAREFUL!!!\nYou are going to login your Wechat on website\nGet your smartphone\nBe ready to scan the 2-D code")
if login==True:
    c.login()
    user=c.search_friends(name='Leo')
    unleo=user[0]['UserName']
    user = c.search_friends(name='Lancelot蒋周羽')
    unlancelot = user[0]['UserName']
    user=c.search_friends(name='Eva')
    uneva=user[0]['UserName']
    user=c.search_friends(name ='Khloe Lu')
    unkhloe=user[0]['UserName']
    #namename='Hagrid周文哲'
    #user=c.search_friends(name=namename)
    #unhagrid=user[0]['UserName']
    user=c.search_friends(name="George浦方一舟")
    ungeorge=user[0]['UserName']
    user=c.search_friends(name='Xu Yizhou')
    unxuyizhou=user[0]['UserName']
    user=c.search_friends(name='Andy周勉')
    unandymian=user[0]['UserName']
    user=c.search_friends(name='Estelle张蕾')
    unestelle=user[0]['UserName']
    user=c.search_friends(name='Olivia')
    unolivia=user[0]['UserName']
    namedic={"Leo":unleo,"Estelle":unestelle,"Andy mian":unandymian,"Khloe Lu":unkhloe,"Eva":uneva,"George":ungeorge,"Lancelot":unlancelot,"Xu Yizhou":unxuyizhou,"Olivia":unolivia}
    def act(text):
        back=False
        if text=="[ELSE:input text]":
            text=g.enterbox(msg="Input the message you want to send to "+name,title="Text")
            if text!=None:
                c.send(text,toUserName=namedic[name])
                back=True
            if text==None:
                back=True
        elif text=="hello？、在吗？":
            c.send("hello？",toUserName=namedic[name])
            c.send("在吗？",toUserName=namedic[name])
            back=True
        elif (text=="thx") or (text=="WOW!"):
            c.send(text,toUserName=namedic[name])
            back=True
        elif text=="[ 3 random 哈哈哈哈]":
            for i in range(3):
                haha="哈"*(random.randint(4,10))
                c.send(haha,toUserName=namedic[name])
            back=True
        return(text,back)
    msg="Select a friend you want to send message to:"
    title="Choose a friend"
    contacts=sorted(["Estelle","Leo","Andy mian","Khloe Lu","Eva","Hagrid","George","Lancelot","Xu Yizhou","Olivia"])
    loop=True
    while loop==True:
        text=None
        while text==None:
            name=g.choicebox(msg=msg,title=title,choices=contacts)
            if name==None:
                break
            back=True
            while back==True:
                back=False
                text=g.choicebox(msg="Choose the message you want to send to "+name,title="Text",choices=txtcho)
                result=act(text)
                print (result)
                text=result[0]
                back=result[1]
        if name!=None:
            loop=g.boolbox(msg="Message Sent to "+name+"\nWanna another loop?",title="",choices=("Run Another Turn","Exit Program"))
        else:
            loop=False
    c.logout()
