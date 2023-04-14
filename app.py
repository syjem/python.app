
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