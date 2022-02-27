for i in range(10):
    print("Hello World!")

print("--------")

for i in range(1,11):
    print("Python")

# Sum of 1 to 10 
total = 0
for i in range(1,11):
    total += i
print(total)

# Sum of n numbers
total = 0
num = int(input("Enter a number "))
for i in range(1, num+1):
    total += i
print(total)

# Sum of digits of a number
total = 0
num = input("Enter a number ")
for i in range(0, len(num)):
    total += int(num[i])
print(total)