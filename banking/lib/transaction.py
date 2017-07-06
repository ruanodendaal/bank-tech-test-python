import time

class Transaction:

    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        self.date = time.strftime("%d/%m/%Y")
