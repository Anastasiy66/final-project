from datetime import datetime

class Operation:
    def __init__(self, amount, category, date, comment="", op_type="traumatized"):
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.comment = comment
        self.op_type = op_type  

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime("%d-%m-%Y"),
            "comment": self.comment,
            "op_type": self.op_type 
        }
