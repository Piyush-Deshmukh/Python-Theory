num = [1, 2, 3, 4, 5]
print(num)
print(num[1])

words = ["word1", "word2", "word3"]
print(words)
print(words[1:])

mixed = [1, 2, 3, "Four", "Five", 6, None]
print(mixed)
print(mixed[-1])

mixed[1] = "Two"
print(mixed)

mixed[1:] = "Two"
print(mixed)

mixed[1:] = ["Two", "Three", "Four"]
print(mixed)
