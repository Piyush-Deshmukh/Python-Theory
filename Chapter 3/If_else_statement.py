# Check eligibility to vote 

age = input("Enter your age ")
age = int(age)
if age >= 18:
    print("----")
    print("You are eligible to vote!")
else:
    print("Sorry you are not eligible to vote!")

# Pass statement
a = int(5)
if a == 5:
    pass
else:
    print("Error!")    

# Nested if-else Statement
# Guess the number correctly
winning_number = 22
num = input("Enter a number between 1 and 100 ")
num = int(num)

if num == winning_number:
    print("You Win!")
else:
    if num > winning_number:
        print("Too High!")
    else:
        print("Too Low!")


# If-elif-else Statement
age = input("Enter your age ")
age = int(age)
if 10>=age>=3:
    print("Your age is between 3 and 10!")
elif 18>=age>10:
    print("Your age is between 10 and 18!")
elif 25>=age>18:
    print("Your age is between 18 and 25!")
else:
    print("You are above 25!")