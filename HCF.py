num1= float(input("Please enter the first value:"))
num2= float(input("Please enter the second value:"))

while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
hcf=num1
print("The HCF is:",hcf)
