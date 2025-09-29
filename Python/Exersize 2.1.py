#Example of f string
quantitiy = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of the item no.{} for {} dollars"
print(myorder.format(quantitiy,itemno,price))
#class exersise
print("\nLet us add some numbers by converting them from strings to intergers")
num1=input("Enter First Number :")
num2=input("Enter Second Number :")
result=f"{int(num1)} + {int(num2)} = {int(num1)+int(num2)}"
print(result)