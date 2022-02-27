# DRY --> Don't Repeat Your Code

import random
winning_number = random.randint(1,100)
guess = 1
num = int(input("Enter a number between 1 and 100 "))
game_over = False

while not game_over:
    if num == winning_number:
        print(f"You Win! and you guessed it in {guess} turns.")
        game_over = True
    else:
        if num > winning_number:
            print("too high")
        else:
            print("too low")
        # The code below has been removed from above if-else statements 
        # according to DRY Coding Principle
        # Many more modifications can be made to reduce code. Think about it!
        guess += 1
        num = int(input("Guess again "))