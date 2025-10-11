print("Enter marks obtained in 5 subjects:")
Bangla = int(input("Bangla: "))
English = int(input("English: "))
Math = int(input("Math: "))
Science = int(input("Science: "))
Social_Science = int(input("Social Science: "))

Total_Marks = Bangla + English + Math + Science + Social_Science
avg = Total_Marks / 5

if avg>=91 and avg<=100:
    print("Grade: A+")
elif avg>=81 and avg<=90:
    print("Grade: A")
elif avg>=71 and avg<=80:
    print("Grade: B+")
elif avg>=61 and avg<=70:
    print("Grade: B")
elif avg>=51 and avg<=60:
    print("Grade: C+")
elif avg>=41 and avg<=50:
    print("Grade: C")
elif avg>=33 and avg<=40:
    print("Grade: D")
elif avg>=21 and avg<=32:
    print("Grade: E")
elif avg>=0 and avg<=20:
    print("Grade: F")
else:
    print("Invalid Input")

