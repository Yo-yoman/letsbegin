

#SNAKE WATER AND GUN GAME 
import random
while True:
    Your_choice=input("enter between snake, gun and water").lower()
    comp_choice=random.choice(["gun","snake","water"])
    if Your_choice==comp_choice:
        print("there is a tie ")
    elif (Your_choice=="gun" and comp_choice=="sanke") or (Your_choice=="snake" and comp_choice=="water") or (Your_choice=="water" and comp_choice=="gun"):
        print("you win!")
        break
    else:
        print("you loose ")   
