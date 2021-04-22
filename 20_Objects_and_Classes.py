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

# HERE