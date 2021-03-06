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

# Creating method for the class - you can have multiple methods per class.
# only the first method is init (similar to constructor in JS)


class Car:
    # docstrings
    def __init__(self, name, color):
        self.car_name = name
        self.car_color = color

    def accel(self):
        print(f"The {self.car_name} accelerates at 199mph")
        print(f"The {self.car_name} is {self.car_color} in color \n")


car_1 = Car('mercedes', 'Silver')
car_2 = Car('BMW', 'Blue')

# car_1.name = 'mercedes'
# car_2.name = 'Benz'

car_1.accel()   # to call a method
car_2.accel()   # to call a method

# print(car_1.car_name)
# print(car_2.car_name)

# to get help with dictionaries
print(help(dict))
print(help(Car))  # to get info about your class Car

# Dealing with Errors
# 1. Syntax Errors - errors due to syntax, using a format/spelling that is inconsistent semicolons, spaces, etc
# 2. Exceptions - code begins to run, then error shows

# PRACTICAL
while True:
    print('Zuri is now Live')
    break  # without the break, it will run an infinite loop


# using try except and else error
def calc(num1, num2):
    return num1/num2


try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    division = calc(num1, num2)
except ZeroDivisionError:  # to capture a ZeroDivisionError and print a self defined error
    print('Error')
    # we can use only except to capture all forms of error
else:
    print("No Type Error")  # comes on if there's no error specified under except
finally:
    print("This would print out irrespective of error")
