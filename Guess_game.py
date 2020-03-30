import sys, random, os, math

print("What is your name?")
name = input()

print("Are you ready to enter this game? If yes type 'YES' if not type 'NO' ")
response = input()

if response.lower() == 'yes':
    number = random.randint(1,20)
    print("I am thinking of a number between 1 to 20")

    for guess_time in range(1,7):
        print("Take a guess")
        guess = int(input())

        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            break

    if guess == number:
        print("Cool the number I have been thinking is "+str(number)+". And you have done it in "+str(guess_time)+" chances!")
    else:
        print("Sorry you ran out of chances, the number I thought was"+str(number))

else:
    print("Oh! You are such a loser, why dont you just go AWAY!!")

    