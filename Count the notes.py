Amount= int(input("Enter the amount: "))

note_1= Amount // 1000
note_2= (Amount % 1000) // 500
note_3= ((Amount % 1000)%500)//100

print("Notes of 1000 taka: ", note_1)
print("Notes of 500 taka: ", note_2)
print("Notes of 100 taka: ", note_3)

