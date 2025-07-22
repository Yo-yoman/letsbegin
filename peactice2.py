def check_account():
        with open("new.txt", "r") as f:
        
         stored_pin=f.readline().strip()
         print(stored_pin)
         stored_balance=float(f.readline().strip())
        return stored_pin,stored_balance
def check_balance():
    Your_pin=input("enter your 4 digit pin")
    stored_pin,stored_balance=check_account()
    if len(Your_pin)==4 and Your_pin==stored_pin:
         print(f"your current balance is {stored_balance} ")
    else:
         print("INVALD PIN!")

def check_deposit():
      Your_pin=input("enter your 4 digit pin")
      stored_pin,stored_balance=check_account()
      if len(Your_pin)==4 and Your_pin==stored_pin:     
           deposit_amount=float(input("Enter your deposit amount"))
           stored_balance+=deposit_amount
           with open("new.txt", "w") as f:
                f.write(f"{stored_pin}\n{stored_balance}\n")

                print("YOUR BALANCE IS", stored_balance)
      else:
            print("Your pin is INVALID!") 

def withdraw_money():
    Your_pin=input("enter your 4 digit pin")
    stored_pin,stored_balance=check_account()
    if len(Your_pin)==4 and Your_pin==stored_pin :     
           with_amount=float(input("Enter your withdraw amount"))
           stored_balance-=with_amount
           with open("new.txt", "w") as f:
                f.write(f"{stored_pin}\n{stored_balance}\n")

                print("YOUR BALANCE IS", stored_balance)
    else:
            print("Your pin is INVALID!") 
def create_newuser():
    with open("new.txt", "w") as f:
            stored_pin=input("enter your new pin")
            stored_balance=float(input("enter your new balance"))
            f.write(f"{stored_pin}\n{stored_balance}\n")
            return stored_pin,stored_balance
      
while True:
   print("\n\t\t-------MENU------")
   print("1) CHECK BALANCE\t2) DEPOSIT MONEY")
   print("3) WITHDRAW MONEY\t4) EXIT")
   print("5) CREATE NEW ACCOUNT")

   select=int(input("ENTER  YOUR  MENU"))

   if select==1:
    check_balance()
   elif select==2:
    check_deposit()
   elif select==3:
    withdraw_money( )
   elif select==4:
    break
   elif select==5:
       create_newuser()
   else:
       print("INVALID RANGE")
       continue