print("Enter Marks Obtained in 3 subjects: ")

math= int(input("Math: "))
eng= int(input("English: "))
Sci= int(input("Science: "))

sum = math + eng + Sci
print("Sum of 3 subjects: ", sum)

per= (sum/300)*100


print(end="Percentage Marks =")
print(per)