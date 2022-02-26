# Comma Separated Input
# 1. Name of User
# 2. A Single Character 

# Output
# 1. User Name Length 
# 2. Count the Character that User Inputs (should be case insensitive)


name, char = input("Enter your Name and a Character ").split(",")
print(f"Length of your name is {len(name)}.")

# Method 1
lower_char = char.lower()
lower_name = name.lower()
print(f"{char} comes {lower_name.count(lower_char)} times.")

# Method 2
print(f"{char} comes {name.lower().count(char.lower())} times.")
