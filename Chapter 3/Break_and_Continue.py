# Break
total = 0
for i in range(10):
    if i == 6:
        break
    total += i
print(total)

# Continue
total = 0
for i in range(10):
    if i == 6:
        continue
    total += i
print(total)