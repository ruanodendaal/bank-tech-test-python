import unittest
import time
from account import Account

class TestFeature(unittest.TestCase):

    def setUp(self):
        self.account = Account(100)

    def test_print_with_one_deposit(self):
        output = "date || credit || debit || balance\n%s || 50 ||  || 150\n" % time.strftime("%d/%m/%Y")
        self.account.deposit(50)
        self.assertEqual(self.account.statement.print_statement(), output)

    def test_print_with_one_withdrawl(self):
        output = "date || credit || debit || balance\n%s ||  || 50 || 50\n" % time.strftime("%d/%m/%Y")
        self.account.withdraw(50)
        self.assertEqual(self.account.statement.print_statement(), output)

    def test_print_with_multiple(self):
        output = "date || credit || debit || balance\n%s ||  || 50 || 70\n%s || 20 ||  || 120\n" % (time.strftime("%d/%m/%Y"), time.strftime("%d/%m/%Y"))
        self.account.deposit(20)
        self.account.withdraw(50)
        self.assertEqual(self.account.statement.print_statement(), output)
