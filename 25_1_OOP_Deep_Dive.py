class Animal:
    animal_type = 'mamma'
    counter = 0

    def __init__(self, name):
        self.name = name
        Animal.counter += 1


