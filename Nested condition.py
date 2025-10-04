num = float(input("Enter a number: "))
if num%1 == 0:
    print(f"{int(num)} is a natural number")
    if num > 0:
        print(f"{int(num)} is a positive number")
    elif num < 0:
        print(f"{int(num)} is a negative number")
    else:
        print(f"{num} is  a zero, a neautral number")
else:
    print(f"{num} is  a decimal number")
    if num>0:
        print(f"{num} is a positive decimal number")
    elif num<0:
        print(f"{num} is a negative decimal number")
    else:
        print(f"{num} is  a zero, a neautral number")



