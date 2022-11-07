# Name: Kevin Holt
# Program: M03_Lab.py
# Date: 2022.11.07 (YMD)

# Overview:
# 	Takes input from user about a vehicle (hard-coded as "Car")
# 	Creates an object from inputted data and prints the object

# Vehicle
# 	Superclass for all types of vehicles
# 	Properties:
#		type

# Automobile
# 	Inherits Vehicle
# 	Properties:
#		year
#		make
#		model
#		doors
#		roof


class Vehicle:
	def __init__(self,newType):
		self.type = newType

	def __str__():
		return "Vehicle Type: " + self.type

class Automobile(Vehicle):
	def __init__(self,newType,newYear,newMake,newModel,newDoors,newRoof):
		Vehicle.__init__(self,newType)
		self.year = newYear
		self.make = newMake
		self.model = newModel
		self.doors = newDoors
		self.roof = newRoof

	def __str__(self):
		return "Vehicle Type:    "+self.type+"\nYear:            "+str(self.year)+"\nMake:            "+self.make+"\nModel:           "+self.model+"\nNumber of Doors: "+str(self.doors)+"\nType of Roof:    "+self.roof

# Start of application


print("---- New Car ----")
print("Please enter the corrosponding information")
print()
print("Year:")
tempYear = input("> ")
print()
print("Make:")
tempMake = input("> ")
print()
print("Model:")
tempModel = input("> ")
print()
print("Number of Doors:")
tempDoors = input("> ")
print()
print("Type of Roof: (Sun-roof, Solid, etc)")
tempRoof = input("> ")
print()

auto = Automobile("Car",int(tempYear),tempMake,tempModel,int(tempDoors),tempRoof)
# auto.year = int(tempYear)
# auto.make = tempMake
# auto.model = tempModel
# auto.doors = int(tempDoors)
# auto.roof = tempRoof

print(auto)
