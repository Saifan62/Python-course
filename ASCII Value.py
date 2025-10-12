ch= input("Enter a character:")

if len(ch) == 1:
    a=ord(ch)
    print("The ASCII value of", ch, "is", a)
    print("Hexadecimal value of", ch, "is", hex(a), "and binary value is", bin(a))
    print("Octal value of", ch, "is", oct(a))
if a >= 65 and a <= 90:
    print(ch, "is an uppercase letter")
elif a >= 97 and a <= 122:
    print(ch, "is a lowercase letter")
elif a >= 48 and a <= 57:
    print(ch, "is a digit")

else:
    print("Please enter a single character")

