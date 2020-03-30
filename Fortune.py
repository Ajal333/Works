import random
import sys

def fortune(name, random_num):
    if random_num == 1:
        print("You are having a very bad time, "+name )
    elif random_num == 2:
        print("You are such a stupid person, "+name)
    elif random_num == 3:
        print("You will find your soulmate soon, "+name)
    elif random_num == 4:
        print("Whatever you do, will never go correct, "+name)
    elif random_num == 5:
        print("You will die single, "+name+"! LOL!!")
    elif random_num == 6:
        print("Oh my god, "+name+", you are gonna die a virgin")
    elif random_num == 7: 
        print("You will have the best years of your life ahead, "+name)
    elif random_num == 8:
        print("You will have worst years of your life ahead, "+name)
    elif random_num == 9:
        print("You will be the last one to survie if the world ends, "+name)

print("What is your name?")
name = input()

print("Are you ready to enter this game? If yes type 'YES' if not type 'NO' ")
response = input()

while True:
    if response == 'YES' or 'yes' or 'Yes':
        r = random.randint(1,9)
        fortune(name, r)
        sys.exit()
    elif response == 'NO' or 'no' or 'No':
        print("Haha, you are such a loser!!")
        sys.exit()
    else:
        print('Wrong input, mate!')
        sys.exit()


