fruits = ["Mango", "Apple", "Grapes", "Orange", "Bananas"]

# Method 1
# fruits.pop() --> Last element will be removed
# fruits.pop(0)

# Method 2
# del fruits[1]

# Method 3
fruits.remove("Apple")

print(fruits)

# Use of in Keyword
if "Grapes" in fruits:
    print("Grapes is Present!")
else:
    print("Not Present!")