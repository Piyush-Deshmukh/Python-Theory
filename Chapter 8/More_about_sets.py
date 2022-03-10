# in Keyword
s = {"a", "b", "c"}

if "a" in s:
    print("Present!")
else:
    print("Not Present!")


# for loop
# Set is Unordered List so will print elements in different order
for i in s:
    print(i)


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
# Union
union = s1 | s2
print(union)

# Intersection
intersection = s1 & s2
print(intersection)
