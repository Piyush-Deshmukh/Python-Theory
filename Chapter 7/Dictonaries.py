# Q - Why we use Dictonaries ?
# A - Bcz Lists are not enough to store real life data


# How can we create Dictonaries ?
# Method 1
user = {"Name" : "Piyush Deshmukh", "Age" : 18, "Language" : "Python"}
print(user)
print(type(user))

# Method 2
# user = dict(Name = "Piyush Deshmukh", Age = 18)
# print(user)

# Method 3
# user = {
#     "Name" : "Piyush Deshmukh",
#     "Age" : 18,
#     "Language" : ["C", "C++", "Java", "Python"]
# }
# print(user)

# Method 4 --> Dictionary inside Dictionary
# user = {
#     "user1" : {
#         "Name" : "Piyush Deshmukh",
#         "Age" : 18,
#         "Language" : ["C", "C++", "Java", "Python"]
#     },
#     "user2" : {
#         "Name" : "Rahul",
#         "Age" : 17,
#         "Language" : ["C", "C++"]
#     }
# }
# print(user)


# How to access data from a Dictonary
# Note - There is no indexing available
print(user["Name"])


# Type of Data we can store in a Dictionary
# Anything


# How to store data in Empty Dictionary
user = {}
user["Name"] = "Piyush Deshmukh"
user["Age"] = 18
user["Language"] = "Python"
print(user)