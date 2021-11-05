import random
import math
x = random.randint(0, 100)
count = 1
while count<6:
 
 # taking guessing number as input
 guess = int(input("Guess a number: "))
 
 # Condition testing
 if x == guess:
        print("Congratulations!!! The number is =",x)
        break
 elif x > guess:
        print("You guessed too small!")
 elif x < guess:
        print("You guessed too high!")
 count +=1
if count==6:
  print("Please Try Again Later!") 