#3 BMI 

def calculate_bmi(Weight,height):
    BMI=Weight/(height* height)
    return BMI

Weight= float(input("Enter your weight in Kg: "))
height=float(input("Enter your height in meters: "))
BMI=print("Your BMI: ",round(calculate_bmi(Weight,height),2))

#2 Calculator

number=int(input("Enter the  number for which you want the multiplication table "))
for i in range (1,11):
    mul=i*number
    print(i,"*",number,"=",mul)




#1
import random
secret_number=random.randint(1,10)
round1=0
while round1 <3:
    number1=int(input("Quess the number (Between 1 to 10):"))
    if number1 ==secret_number :
       print("congrats..You guess correct number")
       break ;
    elif (number1>secret_number):
      print("Too High,Try Again")

    elif number1 <secret_number :
        print("Too Low,Try Again")
        
    elif (number1 >=10) :
       print("enter number from 1 to 10")
       
    round1+=1
    continue
else :
       print("Better luck next time")


     
    
