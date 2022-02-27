i = 1
while i<=10:
    print("Python")
    i += 1

# Question
temp = ""
name = input("Enter your Name ")
i = 0
while i < len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1

# Infinite Loop
while True:
    print("Python")
    # To stop infinite loop press Ctrl + C