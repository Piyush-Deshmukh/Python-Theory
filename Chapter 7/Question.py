user = {}

name = input("Enter your Name ")
age = input("Enter your Age ")
language = input("Enter your Favourite Language separated by comma ").split(",")

user["Name"] = name
user["Age"] = age
user["Language"] = language

for key, value in user.items():
    print(f"{key} : {value}")