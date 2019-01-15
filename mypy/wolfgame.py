import random
import easygui as g
import itchat as c
login=g.boolbox("欢迎使用狼人杀发牌助手\n继续进程需要登录您的微信网页版\n确认登录微信吗？")
if login==True:
    c.login()
    player=['filehelper']
    playersname=['Andy周勉','Leo','Andy Liu','Esther','Jack','Hagrid周文哲','Tania','刘嘉鹏']
    #allfriends=c.get_friends(update=True)[0:]
    #playersname=[]
    #for i in range(len(allfriends)):
        #playersname.append(allfriends[1][Name])
    msg="Choose the players"
    title="Setting"
    playerlist=g.multchoicebox(msg=msg,title=title,choices=playersname)
    for i in range(len(playerlist)):
        user = c.search_friends(name=playerlist[i])
        uname = user[0]['UserName']
        player.append(uname)
    msg="设置各身份人数：(除上帝外共"+str(len(playerlist))+"人)"
    title="设置"
    fields=["设置村民数量：","设置女巫数量：","设置猎人数量：","设置预言家数量：","设置守卫数量：","设置白痴数量：","设置狼人数量：","设置白狼王数量"]
    cardnumber=[0,0,0,0,0,0,0,0]
    while sum(cardnumber)!=len(playerlist):
        cardnumberp=g.multenterbox(msg=msg,title=title,fields=fields)
        for i in range(len(cardnumberp)):
            cardnumber[i]=int(cardnumberp[i])
        msg+="\n输入身份数须与人数相符！"
    villagernumber = cardnumber[0]
    sorceressnumber = cardnumber[1]
    hunternumber = cardnumber[2]
    seernumber = cardnumber[3]
    guardnumber = cardnumber[4]
    idiotnumber = cardnumber[5]
    werewolfnumber = cardnumber[6]
    whitewolfkingnumber = cardnumber[7]
    identitypool = ["God"]
    for i in range(villagernumber):
        identitypool.append ("villager")
    for i in range(sorceressnumber):
        identitypool.append ("sorceress")
    for i in range(hunternumber):
        identitypool.append ("hunter")
    for i in range(seernumber):
        identitypool.append ("seer")
    for i in range(guardnumber):
        identitypool.append ("guard")
    for i in range(idiotnumber):
        identitypool.append ("idiot")
    for i in range(werewolfnumber):
        identitypool.append ("werewolf")
    for i in range(whitewolfkingnumber):
        identitypool.append ("white wolf king")
    totalplayernumber = villagernumber + sorceressnumber + hunternumber + seernumber + guardnumber + idiotnumber + werewolfnumber + whitewolfkingnumber
    msg="total player number (plus God): "+ str(totalplayernumber+1) + "\nThey are:"+str(identitypool)
    g.msgbox(msg=msg)
    goonplaying = True
    while goonplaying == True:
        playersidentity = ["God"]
        cardsleft=totalplayernumber
        identitypoolcopy = identitypool[:]
        for i in range(totalplayernumber):
            card=random.randint(1,cardsleft)
            playersidentity.append(identitypoolcopy[card])
            del identitypoolcopy[card]
            cardsleft-=1
        for i in range(totalplayernumber+1):
            msg="Your identity is:  ["+playersidentity[i]+"]\nKeep it a secret!"
            c.send(msg,toUserName=player[i])
        goonplaying = g.boolbox(msg="continue playing?")
    c.logout()
g.msgbox(msg="Thank you for playing!\nHave a good day!",ok_button="Close")
