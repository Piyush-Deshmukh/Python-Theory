string = "is Python is a High Level Language and it was launched in 1991."

# Replace
print(string.replace(" ","_"))

print(string.replace("Language","Lang"))

print(string.replace("L","l",1))

# Find
print(string.find("is"))

print(string.find("is",1))

# If we don't know where the 2nd "is" is
is_pos1 = string.find("is")
is_pos2 = string.find("is",is_pos1 + 1)
print(is_pos2)