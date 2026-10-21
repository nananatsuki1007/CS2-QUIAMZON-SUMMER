# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")

if name == "":
    print("Looks like it's blank! Fill it out please.")
    name = input("Enter passenger name: ")
    
distance = float(input("Enter distance (km): "))

if distance == 0:
    print("You're kidding, right? Input a number greater than zero.")
    distance = float(input("Enter distance (km): "))
    if distance == 0:
        print("Fine, be stubborn.")

passengers = int(input("Enter number of passengers: "))

if passengers <= 0:
    print("Are we riding with ghosts? Half-people?")
    passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number