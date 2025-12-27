class Car:
    def __init__(self,capacity):
        self.capacity= capacity
    def fare(self):
        return self.capacity * 50
    
class Bus(Car):
    def fare(self):
        base_fare = super().fare()
        total_fare = base_fare + (0.1 * base_fare)
        return total_fare
bus = Bus(50)
print("Total Bus fare is:", bus.fare())