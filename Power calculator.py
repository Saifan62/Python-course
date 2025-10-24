base=int(input("Enter the base number: "))
exponent=int(input("Enter the exponent number: "))

result= base ** exponent
for i in range(exponent):
    result= result * base

print("result is: ", result)