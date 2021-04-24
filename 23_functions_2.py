def name_of_function(count):
    print("This is a function %d" %count)


name_of_function(4)


# Or
def name_of_function(count):
    print(f"This is a function {count}")


name_of_function(4)


# Passing multiple parameters
def name_of_function(name, count):
    print("%s called a function with count %d" %(name, count))


name_of_function('Sam', 4)
name_of_function('Jason', 6)
name_of_function('Rachael', 8)


# To display a string certain number of times
def name_of_function(name, count):
    print(name * count)


name_of_function('Sam ', 4)
name_of_function('Jason ', 6)
name_of_function('Rachael ', 8)
