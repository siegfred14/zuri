class Animal:
    animal_type = 'mamma'
    counter = 0

    def __init__(self, name):
        self.name = name
        Animal.counter += 1


animal_one = Animal('rat')
animal_two = Animal('cat')

