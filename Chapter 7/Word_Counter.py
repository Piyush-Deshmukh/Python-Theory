def word_counter(x):
    count = {}
    for i in x:
        count[i] = x.count(i)
    return count

print(word_counter("piyush deshmukh"))