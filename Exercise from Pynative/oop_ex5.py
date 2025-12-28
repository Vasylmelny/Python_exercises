class Vehicle:

    def __init__(self, name, max_speed, mileage, color = "White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

    def outa(self):
        print(f"Color: {self.color}, Vehicle name: {self.name},Speed: {self.max_speed} Mileage: {self.mileage}")

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# Expected Output:
#
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

Veh1 = Bus("School Volvo", 180, 12)
Veh2 = Car("Audi Q5", 240, 18)

Veh1.outa()
Veh2.outa()