import sys

# positive or negative 
n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

# sequences
name = ["Harry", "Ron", "Ginny"]
print(name[0])

# Tuple
coordinateX = 10.0
coordinateY = 20.0
coordinates = (10.0, 20.0)
print(coordinates)

# lists of names
names = ["Harry", "Ron", "Ginny", "Fred"]
names.append("Draco")
names.sort()
print(names)

# sets
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(5)
s.remove(3)
print(s)
print(f"The set has {len(s)} elements.")

# Loops
for i in range(10):
    print(i)

for name in names:
    print(name)

# dictionaries
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
houses["Ron"] = "Gryffindor"
print(houses["Harry"])
print(houses)

# functions
def square(n):
    return n * n

for i in range(20):
    print(f"The square of {i} is {square(i)}.")

# OOP (classes)
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)


# Add passengers to flight(OOP)
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(5)

people = ["Jem", "Kurt", "Karl", "Michael", "Mark", "Exequel"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

# lambda (functional programming in Python)
cars = [
    {"carName": "BMW", "year": 2000},
    {"carName": "Ford", "year": 1998},
    {"carName": "Tesla", "year": 2010}
]
cars.append({"carName": "Ferrari", "year": 2005})
cars.sort(key=lambda cars: cars["year"])

print(cars)


# Exceptions in Python
try:
    x = int(input("x: "))
    y = int(input("y: "))

except ValueError:
    print("ValueError: Invalid input.")
    sys.exit(1)

try:
    result = x / y
    
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
