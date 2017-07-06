class Statement:

    def __init__(self):
        self.summary = []

    def print_statement(self):
        output = "date || credit || debit || balance\n"
        for i in reversed(self.summary):
            if i.amount > 0:
                output += self.credit(i.date, i.amount, i.balance)
            else:
                output += self.debit(i.date, i.amount, i.balance)
        return output

    def credit(self, date, amount, balance):
        return "%s || %s ||  || %s\n" % (date, amount, balance)

    def debit(self, date, amount, balance):
        return "%s ||  || %s || %s\n" % (date, abs(amount), balance)
