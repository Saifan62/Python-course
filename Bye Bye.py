valid = False
while not valid:
    try:
        n=int(input("Enter a number: "))
        while n%2==0:
            print("Bye Bye")
        valid = True
    except ValueError:
        print("Invalid input, please enter a valid number.")
