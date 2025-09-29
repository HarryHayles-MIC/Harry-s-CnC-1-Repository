#Example Code
age = 26
name = "Harry"
print(f"My name is {name}, my age is {age}")
#grade example
grade=0.76
message= f"{name} recived a grade of {grade:.0%}"
print(message)
#format vaules
value=3.14149
print(f"Value: {value:.2f}")
#input and dectect odd or even using % moudlals opperator
innum=int(input("Enter a Number to see if odd or even: "))
div=innum %2
if div==0:
    print(f"The number {innum} is even")
elif div !=0:
    print(f"The number {innum} is odd")
else:
    print("Invalid entry")