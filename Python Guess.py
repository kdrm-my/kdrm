import random

num = random.randint(1,10)
guess = None

while num != guess:
    guess = input("Enter a number between 1 to 10 :-")
    guess = int(guess)
    
    if num == guess:
        print("You Win!")
    else:
        print("You Loss!")