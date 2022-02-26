# Add two numbers 

# Wrong Method
# a = input("Enter 1st number ")
# b = input("Enter 2nd number ")
# total = a + b 
# print("Sum is " + total)

# Correct Method
a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number "))
total = a + b 
# print("Sum is " + total) --> Error
print("Sum is " + str(total)) # Converted to string as we cannot concatenate a String to a Integer


# str
# 4 --> "4"

# int
# "4" --> 4

# float
# "4" --> 4.0

num1 = str(5)
num2 = float(6)
num3 = int(7)
print(num2 + num3) # Answer in Float