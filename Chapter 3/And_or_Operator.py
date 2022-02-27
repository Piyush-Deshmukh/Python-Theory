# And Operator 
# Condition1   Condition2   Result
#    TRUE         TRUE        TRUE
#    TRUE         FALSE       FALSE
#    FALSE        TRUE        FALSE
#    FALSE        FALSE       FALSE


name = "Piyush"
age = int(18)
if name == "Piyush" and age == 19:
    print("Condition True!")
else:
    print("Condition False!")

# or Operator 
# Condition1   Condition2   Result
#    TRUE         TRUE        TRUE
#    TRUE         FALSE       TRUE
#    FALSE        TRUE        TRUE
#    FALSE        FALSE       FALSE

if name == "Piyush" or age == 19:
    print("Condition True!")
else:
    print("Condition False!")