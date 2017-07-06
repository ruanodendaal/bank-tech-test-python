import unittest
from transaction import Transaction

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction(100, 150)

    def test_default_options_set(self):
        self.assertEqual(self.transaction.amount, 100)
        self.assertEqual(self.transaction.balance, 150)
