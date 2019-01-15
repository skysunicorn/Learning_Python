import random
over = False
while not over:
    answer = random.randint(1,100)
    guess = int(input("have a guess what number I'm thinking about:"))
    for i in range(9):
        if answer == guess or guess == 31415926:
            print("Congratulations! You got it!")
            break;
        elif answer < guess:
            guess = int(input("Too big! Guess again:"))
        else:
            guess = int(input("Too small! Guess again:"))
    else:
        print("Sorry, Hagrid sucks!")
    goon = input("Do you want to go on playing?(yes or no)")
    if goon == "yes":
        over = False
    else:
        goon = True
