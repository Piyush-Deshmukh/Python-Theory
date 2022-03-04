a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(a)
print("--------")


print(a[0])
print("--------")


for list in a:
    print(list)
print("--------")


for list in a:
    for sublist in list:
        print(sublist)
print("--------")


print(a[1][2])
print("--------")

# Type function --> To find type of a object
b = "String"
print(type(b))
print(type(a))