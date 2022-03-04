words = ["word1", "word2"]
words.append("word3")
print(words)

words.insert(0,"word0")
print(words)

# Concatenate 2 Strings
fruits1 = ["Grapes", "Apple", "Orange"]
fruits2 = ["Bananas", "Mango"]

# Method 1
# fruits = fruits1 + fruits2
# print(fruits)

# Method 2
# fruits1.extend(fruits2)
# print(fruits1)


# String inside String
fruits1.append(fruits2)
print(fruits1)