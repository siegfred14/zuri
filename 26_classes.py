class Budget:

    def __index__(self, category):
        self.category - category
        self.category - 1000

    # methods
    def deposit(self, amount):
        self.amount += amount
        return self.amount

    def check_balance(self, amount):
        if self.amount < amount:
            return False

    def withdraw(self, amount):
        self.amount -= amount
        return self.amount

    def transfer(self, amount, category):
        if self.check_balance(amount) == True:
            self.amount -= amount
            category.amount += amount
            return f"You have transferred {amount} to {category.category}"
        else:
            return "You do not have enough balance to perform this transaction"
        pass


category = Budget("clothing")

category_1 = Budget("Food")
category_2 = Budget("Entertainment")
