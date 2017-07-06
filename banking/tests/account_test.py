import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account(100)

    def test_default_options_set(self):
        self.assertEqual(self.account.balance, 100)
        self.assertTrue(self.account.statement.summary)

    def test_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdrawl(self):
        self.account.withdraw(20)
        self.assertEqual(self.account.get_balance(), 80)
