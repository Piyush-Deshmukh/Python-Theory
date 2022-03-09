user = {
    "Name" : "Piyush Deshmukh",
    "Age" : 18,
    "Language" : ["C", "C++", "Java", "Python"]
}


# Check if Key is there or Not
if "Name" in user:
    print("Present!")
else:
    print("Not Present!") 


# Check if Value is there or Not
if 18 in user.values():
    print("Present!")
else:
    print("Not Present!") 


# Values Method
user_values = user.values()
print(user_values)
print(type(user_values))

# Keys Method
user_keys = user.keys()
print(user_keys)
print(type(user_keys))


# Loop in Dictionaries
# Print Keys in Dictionaries
for i in user:
    print(i)

# Print Values in Dictionaries
# Method 1
for i in user.values():
    print(i)

# Method 2
for i in user:
    print(user[i])


# Items Method
user_items = user.items()
print(user_items)
print(type(user_items))

for i in user.items():
    print(i)

for key, value in user.items():
    print(f"The Key is {key} and the Value is {value}")