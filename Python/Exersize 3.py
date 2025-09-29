#Run Box
print("Welcome to Exersize 3")
#Calculator
print("Lets try multiplying two numbers.")
num1=int(input("Enter First Number :"))
num2=int(input("Enter Second Number :"))
result1=num1*num2
print("Your Result is :",result1)
#Circumference
print("Lets find the circumference of a circle")
import math
radius=int(input("Enter Radius:"))
circumference= math.pi*radius**2
print("The Circumference of this circle is ",circumference)
#float
print("Now lets add two floats together")
y=float(input("Enter float Number :"))
x=float(input("Enter float Number :"))
result=x+y
print("Your Result is :",result)
#James
print("My", "Name", "Is", "James")
#Number
print("Now we show how to round a number to 3 decimal places")
z=float(input("Enter a with more than 3 decimal places Number :"))
round_z= round(z,3)
print("Your number is: ",round_z)
#name
print("We will now experiment with input of strings.")
firstName=input("Enter your First Name :")
lastName=input("Enter Your Last Name:")
print(lastName,firstName)
print(lastName,"-",firstName)
#Football
print("This is to a different way to print using f strings")
totalMoney = 1000
quantity = 3
price = 450
football= f"I have {totalMoney} Dollars, so I can buy {quantity} footballs for {price} dollars each"
print(football)