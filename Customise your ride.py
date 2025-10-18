print("Select your ride type:")
print("1. Bike")
print("2. Car")

choice= int(input("Enter your choice (1 or 2): "))

if( choice == 1):
    print("What type of bike would you like?")
    print("a. Standard Bike")
    print("b. Sports Bike")
    bike_type= input("Enter your choice (a or b): ")
    if(bike_type == 'a'):
        print("You have selected a Standard Bike.")
    elif(bike_type == 'b'):
        print("You have selected a Sports Bike.")
elif( choice == 2):
    print("What type of car would you like?")
    print("a. Sedan")
    print("b. SUV")
    car_type= input("Enter your choice (a or b): ")
    if(car_type == 'a'):
        print("You have selected a Sedan.")
    elif(car_type == 'b'):
        print("You have selected an SUV.")

else:
    print("Invalid choice. Please select either 1 or 2.")
