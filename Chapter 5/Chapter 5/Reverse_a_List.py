# Method 1
# def rev(x):
#     x.reverse()
#     return x

# Method 2
# def rev(x):
#     return x[::-1]

# Method 3
def rev(x):
    reverse = []
    for i in range(len(x)):
        reverse.append(x.pop())
    return reverse

num = [1, 2, 3, 4, 5]
print(rev(num))