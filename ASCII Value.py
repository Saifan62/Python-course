name=input("Please enter a character: ")
if len(name) == 1:
    ascii_value = ord(name)
    print(f"The ASCII value of '{name}' is {ascii_value}.")
elif len(name) > 1:
    print("Please enter only a single character.")
    
else:
    print("Invalid input. Please enter a single character.")