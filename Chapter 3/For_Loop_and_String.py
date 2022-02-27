lang = "Python"

# Method 1
for i in range(len(lang)):
    print(lang[i])
print("-------")

# Method 2
for i in lang:
    print(i)
print("-------")

# Method 3
for i in "PYTHON LANGUAGE":
    print(i)


# Sum of digits of number
num = input("Enter a number ")
total = 0
for i in num:
    total += int(i)
print(total)