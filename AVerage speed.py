a= int(input("Enter a value: "))
b= int(input("Enter another value: "))
c= int(input("Enter one more value: "))
average_speed = (a + b + c) / 3
print("The average speed is:", average_speed)

if average_speed > a and average_speed > b and average_speed > c:
    print("%d is higher than %d,%d,%d."% (average_speed, a, b, c))
elif average_speed < a and average_speed < b :
    print("%d is higher than %d,%d."% (average_speed, a, b))
elif average_speed < a and average_speed < b :
    print("%d is higher than %d,%d."% (average_speed, a, c))
elif average_speed < a and average_speed < b :
    print("%d is higher than %d,%d."% (average_speed, b, c))
elif average_speed < a and average_speed < b :
    print("%d is higher than %d."% (average_speed, a,))
elif average_speed < a and average_speed < b :
    print("%d is higher than %d."% (average_speed, b,))
elif average_speed < a and average_speed < b :
    print("%d is higher than %d."% (average_speed, c,))
else:
    print("Invalid Input")
