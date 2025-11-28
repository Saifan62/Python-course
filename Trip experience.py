def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if 'Charlotte' == city:
        return 183
    elif 'Tampa' == city:
        return 220
    elif 'Pittsburgh' == city:
        return 222
    elif 'Los Angeles' == city:
        return 475
    
def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return days * 40
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("Total trip cost:",trip_cost("Los Angeles",5,8000))
