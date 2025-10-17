print("Enter a NUmber (Numerator):")
numn=int(input())
print("Enter a Number (Denominator):")
denom=int(input())
if numn % denom==0:
    print("\n" +str(numn)+ "is divisible by " +str(denom))
else:
    print("\n" +str(numn)+ "is not divisible by " +str(denom))
    