def add(x,y):
    return x + y 

a, b = input("Enter two numbers ").split()
a = int(a)
b = int(b)
print(add(a,b))

c, d = "Hello ", "World"
print(add(c,d))

# Odd or Even number
def is_even(num):
    return num%2==0

print(is_even(5))

# Palindrome 
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("naman"))
print(is_palindrome("madam"))
print(is_palindrome("python"))