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

