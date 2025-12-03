start= int(input("Enter the starting number: "))
end= int(input("Enter the ending number: "))

squares = []
odd=[]
even=[]

for i in range(start, end + 1):
    squares.append(i * i)
    if i * i % 2 != 0:
        odd.append(i * i)
    else:
        even.append(i * i)

print(f"Squares from {start} to {end}: {squares}")
print(f"Odd squares: {odd}")
print(f"Even squares: {even}")

