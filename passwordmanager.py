while True:
  import random
  def pas():
  
   user_pass=int(input("enter how long the password should you want ")) 
   password="" 

   i=0
   for i in range(user_pass):
    user=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#%&*!?<>+")
    password+=user
    i=i+1
    
   return password

  save=pas()
  print(save)
  with open("save.txt","w") as f:
    f.write(save)
   