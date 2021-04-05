# Focus
# register
# login

# Dictionary - called object in other languages - carries key value pairs
aSampleList = [1,2,3,4,5]

# method 1 for dictionary

dictionaryOne = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'
}

# method 2 - here we add the key values pairs manually
dictionaryTwo = {}

# to add key value pairs
dictionaryTwo['key4'] = 'value4'
dictionaryTwo['key5'] = 'value5'
dictionaryTwo['key6'] = 'value6'

print(dictionaryOne)
print(dictionaryTwo)

# To delete from a dictionary
del dictionaryTwo["key4"]

print(dictionaryTwo)

# Alternative method to delete from dictionary
dictionaryOne.pop('key1')

print(dictionaryOne)

# How to loop through items in a dictionary
    #for
for key,value in dictionaryOne.items():
    print("I have " + key + " relating with " + value)
    print(f"I have {key} relating to {value}")
    print("=======")

    # Kanjii Mbugua - I will go