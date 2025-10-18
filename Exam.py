medical_cause=input("Enter the medical cause: ")
atten=int(input("Enter the attendance of the student: "))

if medical_cause=="Y":
    print("You are allowed")
else:
    if atten>=75:
        print("You are allowed")
    else:
        print("You are not allowed")


