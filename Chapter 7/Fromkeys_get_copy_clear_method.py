# fromkeys

# user = dict.fromkeys(["Name", "Age", "Language"], "Unknown")
# print(user)

# user = dict.fromkeys(("Name", "Age", "Language"), "Unknown")
# print(user)

# user = dict.fromkeys(["Name", "Age", "Language"], ["Unknown", "Unknown"])
# print(user)


# get Method
user = {"Name" : "Piyush Deshmukh", "Age" : 18, "Language" : ["C", "C++", "Java", "Python"]}
print(user.get("Name"))
print(user.get("Names"))
print(user.get("Names", "Not Found!"))


# clear Method
# user.clear()
# print(user)


# copy Method
a = user.copy()
print(user.popitem())
print(a)