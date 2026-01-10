# WAP to stimulate the rolling of a die,
# also ask the user if they want to continue or not.
import random
print("Welcome to 'Rolling A die', make your choice :D\n")
while True:
    choice=input("Yes/Enter: if you want to continue\nNo: if you want to exit\nYour choice:")
    if choice=="Yes" or choice=='yes' or choice=='':
        print(f"Your number is:{random.randint(1,6)}\n")
    elif choice=="No" or choice=="no":
        print("Exiting...")
        break
    else:
        print("Please enter Yes or No")
