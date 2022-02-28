# No Error
def info(first_name, last_name, age):
    print(f"Your First Name is {first_name}")
    print(f"Your Last Name is {last_name}")
    print(f"Your Age is {age}")

# Error
# def info(first_name, last_name = "Unknown", age):
#     print(f"Your First Name is {first_name}")
#     print(f"Your Last Name is {last_name}")
#     print(f"Your Age is {age}")

# Error
# def info(first_name = "Unknown", last_name, age):
#     print(f"Your First Name is {first_name}")
#     print(f"Your Last Name is {last_name}")
#     print(f"Your Age is {age}")

# No Error
def info(first_name, last_name, age = None):
    print(f"Your First Name is {first_name}")
    print(f"Your Last Name is {last_name}")
    print(f"Your Age is {age}")

# No Error
def info(first_name, last_name = "Unknown", age = None):
    print(f"Your First Name is {first_name}")
    print(f"Your Last Name is {last_name}")
    print(f"Your Age is {age}")

# No Error
def info(first_name = "Unknown", last_name = "Unknown", age = None):
    print(f"Your First Name is {first_name}")
    print(f"Your Last Name is {last_name}")
    print(f"Your Age is {age}")

# Error
# def info(first_name = "Unknown", last_name, age = None):
#     print(f"Your First Name is {first_name}")
#     print(f"Your Last Name is {last_name}")
#     print(f"Your Age is {age}")

