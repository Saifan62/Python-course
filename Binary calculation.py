def DecimalToBinary(num):
    if num>=1:
        DecimalToBinary(num//2)
    print(num % 2,end='')

print("Binary of 5 is: ",end='')
DecimalToBinary(5)
print()

print("Binary of 23 is: ",end='')
DecimalToBinary(23)
print()

print("Binary of 50 is: ",end='')
DecimalToBinary(50)
print()

print("Binary of 100 is: ",end='')
DecimalToBinary(100)
print()
