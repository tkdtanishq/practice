# Create a simple number guessing game.
# The user get 10 chances to guess the number, range: ask the user
# if the user guesses the number before the given 10 chances:
#     1.stop asking the number from the user
#     2.say congrats and end the game
# if the user never guesses the number, ask them 10 times and then end the game!!

import random
print('-'*18+'GAME START: GUESS THE NUMBER'+'-'*18)
na=input("Enter your name:")
b,e=int(input("Enter the beginning of the range:")),(int(input("Enter the end of the range:")))
name=na.upper()
r=random.randint(b,e)
print(f"The SECRET NUMBER is between {b} and {e}\n")
q=10
for i in range(1,11):
    print(f"You have {q} attempts left.")
    n=int(input("Enter your guess:"))
    if b<=n<=e:
        if n!=r:
            if n>r:
                print("Your guess is WRONG, Try LOWER.\n")
            elif n<r:
                print("Your guess is WRONG, Try HIGHER.\n")
            q-=1
            if q==0:
                print(f"{name} has used all the guesses.\nPOOR PERFORMANCE :( \nThe secret number was:{r}\nGAME OVER!!")
                print("-"*64)
        elif n==r:
            print(f"CONGRATULATIONS {name}!! YOU HAVE GUESSED THE SECRET NUMBER :D")
            print("-"*64)
            break
    else:
        print("--->OUT OF RANGE<---\n")
