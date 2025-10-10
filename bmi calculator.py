height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight : "))

BmI = weight / (height / 100) ** 2
print("Your BMI is ", BmI)

if BmI <= 18.5:
    print("You are underweight")    
elif BmI <= 24.9:
    print("You have a normal weight")
elif BmI <= 29.9:
    print("You are overweight")
elif BmI <= 34.9:
    print("You are severely overweight")
elif BmI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")

