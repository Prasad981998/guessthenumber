"""we have to guess the random number if the number matches it will shows number of attempts to guess correct number"""

import random
lower=int(input("please enter lower level:"))
upper=int(input("please enter upper level:"))
number=random.randint(lower,upper)
guess=int(input("please enter guess:"))
count=1
for i in range(lower,upper):
    if guess > number:
        guess=int(input("please enter lower number than guess:"))
        count=count+1
        
    elif guess < number:
        guess=int(input("please enter upper number than guess:"))
        count=count+1
        
    elif guess == number:
        pass
    
print("you have entered correct number:", guess, "and total number of attempts is:",count)