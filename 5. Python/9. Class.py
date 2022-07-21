# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2, 9)

# print(p.x)
# print(p.y)

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
            self.passengers.append(name)

flight = Flight(12)
passenger = ["Harry", "Ron", "Hermoine", "Draco"]
for passe in passenger:
    if flight.add_passenger(passe):
        print(f"Passenger {passe} add successfully!")
    else:
        print(f"No seats Available for {passe}!")