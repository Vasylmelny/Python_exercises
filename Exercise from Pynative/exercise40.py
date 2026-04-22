# Create a Car class with attributes for make, model, and year.
# Include a method called start_engine()
# that prints a formatted string describing the car starting up.

class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

p1 = Car("Germaby", "Vectra", 1978)

print(p1.make)
print(p1.model)
print(p1.year)