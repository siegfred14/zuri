# FUNCTIONS
# A function is a block of codes which only runs when called

def simple_function():
    print('This is my first function!')

# to call the function
simple_function()

# parameters are added to the function, then called as arguments

# def simple_function(name):
#     print(f"Hello {name}")
#
# name_input = input("enter your name: ")
#
# simple_function(name_input) # function call


# You can have multiple parameters for your function
# def simple_function(firstName, lastName):
#     print(f"Hello {firstName} are you sure your Last Name is {lastName}")


# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")
#
# simple_function(first_name, last_name)

# for proper practice, let your function handle one thing

# Arbitrary argument - args return tuples
# def people_names(*args):
#     print(args)


# first_name = input("enter your first name: ")
# last_name = input("enter your last name: ")

# simple_function(first_name, last_name)
#people_names(first_name, last_name)

print('===============')


# using args
# def people_names(first_name, *args):
#     print(first_name)
#     last_name, middle_name = args
#     print(last_name)
#     print(type(args))


# first_name = 'Manny'
# last_name = 'Johnson'
# middle_name = 'Devs'

# simple_function(first_name, last_name)


# Using Named Arguments - this allows you to call your arguments at random
def people_names(firstname, lastname, middlename):
    print(firstname)
    print(lastname)
    print(middlename)


first_name = 'Manny'
last_name = 'Johnson'
middle_name = 'Devs'

# people_names(first_name, last_name, middle_name) # normal call
people_names(middlename = middle_name, lastname=last_name, firstname=first_name) # normal call

