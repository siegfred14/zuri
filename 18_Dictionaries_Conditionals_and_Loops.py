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

