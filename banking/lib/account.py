from statement import Statement
from transaction import Transaction

class Account:

    def __init__(self, balance = 0):
        self.balance = balance
        self.statement = Statement()

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        transaction = Transaction(amount, self.balance)
        self.update_statement(transaction)

    def withdraw(self, amount):
        self.balance -= amount
        transaction = Transaction(-amount, self.balance)
        self.update_statement(transaction)

    def update_statement(self, transaction):
        self.statement.summary.append(transaction)
