#Example to print a random number:
import random #import the random class
#the base score
score=0
#program start
print("welcome to my random number program\n")
print("Generating a random number between 1 and 10 :",random.randint(1,10),"\n")

#Exersize 1
print("Now Lets Run Exersize 1, where we run a small prediction\n")
oracle=random.randint(1,6)
user_guess=int(input(f"What do you thing your luck is today? \n Please Enter a Number between 1 and 6, if you get it correct I will reveal the future:"))
if oracle == 1 and user_guess == 1:
    print("\nYou will have a great day")
elif oracle == 2 and user_guess == 2:
    print("\nYou will see a lucky star")
elif oracle == 3 and user_guess == 3:
    print("\nYou might get a winning ticket")
elif oracle == 4 and user_guess == 4:
    print("\nA Good Day to play lotto")
elif oracle == 5 and user_guess == 5:
    print("\nJust an ordinary day")
elif oracle == 6 and user_guess == 6:
    print("\nOr maybe not so..")
elif user_guess != oracle :
    print("\nThe Oracle will not reveal their answer, try again\n")

#Exersize 2
print("Now Lets Run Exersize 2, Lets see how good at math you are\n")

#calcualte 2 numbers between 1 and 50
num1=random.randint(1,50)
num2=random.randint(1,50)
#Correct answer of the sum
correct_ans=num1+num2
#user answer input
user_ans=int(input(f"Please find the sum of {num1} + {num2} = "))
#Check if it is true
if user_ans == correct_ans :
    print("Correct. Good Job!")
    score=score+1
else:
    print("Incorrect. Correct answer is ",correct_ans)


rnum1=random.randint(1,20)
rnum2=random.randint(1,20)
rnum3=random.randint(1,20)
#Correct Ans
correct_ans2= rnum1 + rnum2 + rnum3
#user input
user_ans2=int(input(f"Please find the sum of {rnum1} + {rnum2} + {rnum3} = "))
#are they correct
if user_ans2 == correct_ans2 :
    print("Correct. Good Job!")
    score = score + 1
else:
    print("Incorrect. Correct answer is ",correct_ans2)

#lets try multiplication
snum1=random.randint(1,20)
snum2=random.randint(1,20)

correct_ans3 = snum1-snum2

user_ans3=int(input(f"Please find the sum of {snum1} - {snum2} = "))
if user_ans3 == correct_ans3 :
    print("Correct. Good Job!")
    score = score + 1
else:
    print("Incorrect. Correct answer is ",correct_ans3)
#lets try multiplication
mnum1=random.randint(1,10)
mnum2=random.randint(1,10)

correct_ans4 = mnum1*mnum2

user_ans4=int(input(f"Please find the sum of {mnum1} * {mnum2} = "))

if user_ans4 == correct_ans4 :
    print("Correct. Good Job!")
    score = score + 1
else:
    print("Incorrect. Correct answer is ",correct_ans4)

#time for some division
dnum1 = random.randint(1, 10)
dnum2 = random.randint(1, 10)

correct_ans5 = float(dnum1/dnum2)

user_ans5 = float(input(f"Please find the sum of to 2 decimal places. {dnum1}/{dnum2} = "))

if user_ans5 == correct_ans5:
    print("Correct. Good Job!")
    score = score + 1
else:
    print(f"Incorrect. Correct answer is  {correct_ans5:.2}")

print(f"Your score is {score}/5 correct")

