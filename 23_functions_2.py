def nameOfFunction(count):
    print("This is a function %d" %count)


nameOfFunction(4)

# Or
def nameOfFunction(count):
    print(f"This is a function {count}")

nameOfFunction(4)

# Passing multiple parameters
def nameOfFunction(name, count):
    print("%s called a function with count %d" %(name, count))

nameOfFunction('Sam', 4)
nameOfFunction('Jason', 6)
nameOfFunction('Rachael', 8)

