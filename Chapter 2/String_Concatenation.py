# Method 1 for Adding Spaces
a = "Hello"
b = "World"
c = a + " " + b 
print(c)

# Method 2 for Adding Spaces
a = "Hello "
b = "World"
c = a + b 
print(c)

# print(c + 2)  --> Error
print(c + "2")
print(c + str(2))

print(c * 3)