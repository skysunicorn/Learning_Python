import random
while True:
    cardpool=[]
    for i in range(4):
        for j in range(13):
            cardpool.append(str(j+1))
    drawcard=[]
    for i in range(4):
        cardn=0
        cardn=random.randint(0,51-i)
        drawcard.append(cardpool[cardn])
        del cardpool[cardn]
    for i in range(4):
        print(drawcard[i])
    goon=input("Wanna another turn?")
    if goon=="no":
        break
print("Tank you for playing")
    
