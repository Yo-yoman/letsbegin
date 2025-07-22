#BODY MASS INDEX
while True:
 BOdy_wt=float(input("enter your weight in kg  "))
 Body_ht=float(input("enter your height in feet"))
 Body_ht=Body_ht*0.3048
 your_body= BOdy_wt/(Body_ht**2)
 if your_body<18.5:
  print(f"your body wt is {your_body} You need to eat more, underweight")
 elif your_body >= 18.5 and your_body < 24.9:
  print(f"your body wt is {your_body} You are of normal weight, maintain this")
 elif your_body >= 25 and your_body < 29.9:
   print(f"your body wt is {your_body} You need to eat less, have a healthy diet")
 else: 
    print(f"your body wt is {your_body} You are obese, cut your calories to bare minimum")
