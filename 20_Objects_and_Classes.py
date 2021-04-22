# CLASSES
# Classes provide means by which we bundle related data functionalities together
# Transmission of real life scenario into programming

# class - car
# objects - audi, nissan, volvo
# properties - colour, transmission type, max speed
# methods - start - stop, accelerate, change transmission

# Attributes - properties affiliated with a given class
# Methods - functions affiliated with some class
# Instance - object created through calling of that class


class Car:
    pass


print(type(Car))

# To create a car / instantiate a car object
car_1 = Car()

print(type(car_1))


# Setting attributes of a class
class Car:
    pass
    # def __init__(self, name, color):


car_1 = Car()
car_2 = Car()
car_1.name = 'mercedes'
car_2.name = 'Benz'
print(car_1.name)
print(car_2.name)

# This is cumbersome when you have to create attributes for many classes

# Using the init method - above, it is represented by


class Car:
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color


car_1 = Car('mercedes', 'Silver')
car_2 = Car('BMW', 'Blue')

# car_1.name = 'mercedes'
# car_2.name = 'Benz'

print(car_1.car_name)
print(car_2.car_name)

