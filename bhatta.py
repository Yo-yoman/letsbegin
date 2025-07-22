
#GAME 1


import random

computr_choice=random.randint(1,10)
while True:
    user=int(input("enter your choice between 1-10"))
    if( user==computr_choice):
     print("you won the match")
     break 
    elif user<computr_choice :
     print("guesss the larger value")
    else:
     print("guess the smalller  value")    

     print("GAME OVER !")

#GAME 2 


import random
while True:
     choices = ["rock","paper","seasor"]
     computr_choice=choices[random.randint(0,2)]
     user=input("enter rock seasor and paper ")
     user.lower()
     if user==computr_choice:
      print("there is a tie ")
     elif user=="rock" and computr_choice=="seasor" or user=="seasor" and computr_choice=="paper" or user=="paper" and computr_choice=="rock":
      print("you are the winner ")
      break
     else:
      print("better luck! next time")    







   

























