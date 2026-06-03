class Expense:
    def __init__(self, id, category, amount):
        self.id = id
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.id}. {self.category} - ₹{self.amount}"