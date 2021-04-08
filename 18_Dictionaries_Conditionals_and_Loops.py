# Dictionaries
# Ways to define dictionaries

first_variable = {}
second_variable = dict()

print(type(first_variable))
print(type(second_variable))

fruit_basket = {
    "mango": 40,
    "oranges": 30,
    "pawpaw": 3,
    "pineapple": [40, 30, 50, 70]
}

print(len(first_variable))
print(len(second_variable))
print(len(fruit_basket))

# unlike lists, dictionaries do not hold duplicate keys
# dictionaries do not hold only primitive data types, they also hold lists classes, etc

print(isinstance(fruit_basket, dict)) #To check if fruit_basket is an instance of a dictionary data type

# Dictionary values can be accessed using their keys
mangoes = fruit_basket["mango"]
print(mangoes)
print("we have {} mangoes".format(mangoes))

# if we use a value that is in-existent, we can use 'get'
# mangoes = fruit_basket["apples"] #error

mangoes = fruit_basket.get("apples", 0)
print("we have {} apples".format(mangoes))

# To see all keys in the dictionary
all_fruit_keys = fruit_basket.keys()
print(all_fruit_keys)

# To update a particular key from a dictionary
new_fruit_basket = fruit_basket["mango"] - 1
print(new_fruit_basket)

# or
fruit_basket["mango"] = fruit_basket["mango"] - 1
print(fruit_basket)

# updating our dictionary to add new objects
fruit_basket.update({"apples": 35})
print(fruit_basket)

# To get all keys in the basket
print(fruit_basket.items()) #gives you a list of tuples

# to check if a key exists in the dictionary

if "apples" in fruit_basket:
    print(True)

# to remove a key in the dictionary
fruit_basket.pop("oranges")
print(fruit_basket)

# another way to remove a key is
# del fruit_basket["pineapples"]

# to clear all keys in the dictionary
# fruit_basket.clear()

# to delete the dictionary (basket) entirely
# del fruit_basket


# copying of dictionaries
fruit_basket = {
    "mango": 40,
    "oranges": 30,
    "pawpaw": 3,
    "pineapple": {"good": 30, "bad": 34}
}

new_fruit_basket = fruit_basket
print("New Fruit Basket is", new_fruit_basket)
print("Fruit Basket is", fruit_basket)

print(id(fruit_basket))
print(id(new_fruit_basket))
# this doesn't effectively copy. it is just a pointer


# types of copy
# Shallow Copy

new_fruit_basket2 = fruit_basket.copy()
print(fruit_basket)
print(new_fruit_basket2)


print(id(new_fruit_basket2))

# Deep copy
import copy

new_fruit_basket3 = copy.deepcopy(fruit_basket)
print(new_fruit_basket3)


print("===============")
# if a key is updated, copy would be updated as well, but deep copy will not
# This is because deepcopy creates a new independent instance
fruit_basket["pineapple"]["good"] = 25
print(new_fruit_basket2)
print(new_fruit_basket3)

# CONDITIONALS
# number = int(input("Enter a new number" ))
number = 10

# if number > 10:
#     print("yes, number is greater or equals to 10")
# elif number == 10:
#     print("yes, number is equal than 10")
# else:
#     print(f"{number} is not equal to 10")

# A different approach
print(True if number > 10 else False)

print("================== \n")

