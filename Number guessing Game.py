import math
import random

count = 0
lower = int(input("Enter the lower boundry: "))
upper = int(input("Enter the upper booundry: "))

x = random.randint(lower,upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

while(count < math.log(upper - lower + 1, 2)):
    guess = int(input("Guess a number: "))
    count += 1

    if(guess > x):
        print("Try Again! You guessed too high")
        
    if(guess < x):
        print("Try Again! You guessed too small")

    if(guess == x):
        print("Congratulations! you did it in ",count , "try")

if(count >= round(math.log(upper - lower + 1, 2))):
    print("\tBetter Luck Next time!")