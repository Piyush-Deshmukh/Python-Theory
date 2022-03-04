def sublist_counter(x):
    count = 0
    for sublist in x:
        if type(sublist) == list:
            count += 1
    return count

a = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print(sublist_counter(a))