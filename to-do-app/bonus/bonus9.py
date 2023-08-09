password = input("Enter new password: ")
result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# digit = False
# for char in password:
#     if char.isdigit():
#         digit = True
# result["digits"] = digit
result["digits"] = any([True if char.isdigit() else False for char in password])

# uppercase = False
# for char in password:
#     if char.isupper():
#         uppercase = True
# result["uppercase"] = uppercase
result["uppercase"] = any([True if char.isupper() else False for char in password])

print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
