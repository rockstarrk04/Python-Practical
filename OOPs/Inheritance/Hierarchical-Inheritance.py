# Hierarchical Inheritance
#? one parent , multiple children

# Todo : Example 1
class Vehicle:   #! parent
    def Start(self):
        print("Vehicles start")

class Car(Vehicle): #! child1
    def drive(self):
        print("Car has 4 wheels")

class Bike(Vehicle):    #! child2
    def ride(self):
        print("Bike has 2 wheels")

# c = Car()
# c.drive()
# c.Start()

# b = Bike()
# b.ride()
# b.Start()

#==============================================================

# Todo : Example 2

class Animal:
    def eat(self):
        print("All animals eat")

class Dog(Animal):
    def bark(self):
        print("Dogs can bark")

class Cat(Animal):
    def meow(self):
        print("Cats can meow")

# d = Dog()
# d.bark()
# d.eat()

# c = Cat()
# c.meow()
# c.eat()
