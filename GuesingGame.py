import random

highest = 10
answer = random.randrange(highest)
guess = input(f"Gues a number from {highest}: ")
while(int(guess) != answer):
    if(int(guess) < answer):
        print("Answer is Higher")
    else:
        print("Answer is lower")

    guess = input(f"Guess a number from 0 to {highest}: ")

input("You are a winner")