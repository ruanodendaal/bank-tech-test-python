class Statement:

    def __init__(self):
        self.summary = []

    def print_statement(self):
        output = "date || credit || debit || balance\n"
        for i in reversed(self.summary):
            if i.amount > 0:
                output += self.credit(i.amount, i.balance)
            else:
                output += self.debit(i.amount, i.balance)
        return output

    def credit(self, amount, balance):
        return "06/07/2017 || %s ||  || %s\n" % (amount, balance)

    def debit(self, amount, balance):
        return "||  || %s || %s\n" % (amount, balance)
