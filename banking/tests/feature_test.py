import unittest
from account import Account

class TestFeature(unittest.TestCase):

    def setUp(self):
        self.account = Account(100)

    def test_print(self):
        output = "date || credit || debit || balance\n 06/07/2017 || 50 ||  || 150\n"
        self.account.deposit(50)
        self.assertEqual(self.account.statement.print_statement(), output)
