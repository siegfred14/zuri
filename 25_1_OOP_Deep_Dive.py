class Animal:
    animal_type = 'mammal'
    counter = 0

    def __init__(self, name):
        self.name = name
        Animal.counter += 1


animal_one = Animal('rat')
animal_two = Animal('cat')

print(animal_one.animal_type)
print(animal_two.animal_type)


#to check how many times an object is being instanciated/clled in a program
print(Animal.counter)