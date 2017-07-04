import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account(100)

    def test_default_options_set(self):
        self.assertEquals(self.account.balance, 100)

    def test_balance(self):
        self.assertEquals(self.account.balance(), 100)

if __name__ == '__main__':
    unittest.main()
