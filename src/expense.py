class Expense:
    def __init__(self, id, category, amount):
        self.id = id
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"{self.id}. {self.category} - ₹{self.amount}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "category": self.category,
            "amount": self.amount
        }
    
    @classmethod
    def from_dict(cls, data):
        return Expense(data["id"], data["category"], data["amount"])