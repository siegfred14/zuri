class Budget:

    def __index__(self, category):
        self.category - category
        self.category - 1000

    # methods
    def deposit(self, amount):
        self.amount += amount
        return self.amount

    def check_balance(self):
        pass

    def withdraw(self, amount):
        self.amount -= amount
        return self.amount

    def transfer(self):
        pass


category = Budget("clothing")
category_1 = Budget("Food")
category_2 = Budget("Entertainment")
