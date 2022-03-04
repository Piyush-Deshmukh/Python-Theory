# Generate Lists with Range Functions
# numbers = list(range(1,11))
# print(numbers)
numbers = [1, 2, 3, 1, 5, 8, 1, 10, 7, 9]

# More about Pop method
# print(numbers.pop()) --> It prints the number it poped
# print(numbers)

# Index Method
# print(numbers.index(1,2,5)) --> Finds 1 in the range 2 - 5

# Pass List to a Function
def negative_list(x):
    negative = []
    for i in x:
        negative.append(-i)
    return negative

print(negative_list(numbers))

# Min and Max Function
print(min(numbers)) # --> Finds minimum number
print(max(numbers)) # --> Finds maximum number