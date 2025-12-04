print("Mirrored half pyramid pattern of stars (*): ")
n = int(input("Enter the number of rows: "))

for i in range(n):
    
    for s in range(n - i - 1):
        print(" ", end=" ")
    
    for j in range(i + 1):
        print("*", end=" ")
    print()