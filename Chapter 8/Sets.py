# set data type
# Unordered collection of UNIQUE items

s = {1, 2, 3, 1}
print(s) # --> 1 will not be printed according to definition

# print(s[1]) --> Error

# Remove Duplicate
a = [1, 2, 3, 1, 5, 4, 5, 3, 6, 2]
b = list(set(a))
print(b)

# Add element to set
s.add(4)
s.add(5)
print(s)

# Remove a element
# Method 1
s.remove(5)
print(s)

# Method 2
s.discard(4)
print(s)
s.discard(6)
print(s)


# Clear set
# s.clear()
# print(s)

# Copy set
# s1 = s.copy()
# print(s1)

# Set cannot store list and dictionary
s = {1, 2, 3, 2.6, 1.0, "String"} # --> Treats 1 and 1.0 same 
print(s)