import random
def normal():
    states=["rock","paper","scissors"]

    #Gets inputs
    user=input("Pick rock, paper or scissors: ").lower()
    cpu=random.randint(0,2)

    print("The computer chose: "+str(states[cpu]))
    #Converts word version into numbers
    for x in range(0,3):
        if user==states[x]:
            user_num=x

    #Decision logic
    if user_num==cpu:
        print("Draw")
    elif user==states[cpu-1]:
        print("Defeat")
    else:
        print("Victory")

def lizard_spock():
    states=["rock","paper","scissors","lizard","spock"]

    #Gets inputs
    user=input("Pick rock, paper, scissors, lizard or spock: ").lower()
    cpu=random.randint(0,2)

    print("The computer chose: "+str(states[cpu]))
    #Converts word version into numbers
    for x in range(0,3):
        if user==states[x]:
            user_num=x

    #Decision logic
    if user_num==cpu:
        print("Draw")
    elif user==states[cpu-1]:
        print("Defeat")
    else:
        print("Victory")