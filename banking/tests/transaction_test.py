import unittest
import time
from transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction(100, 150)

    def test_default_options_set(self):
        self.assertEqual(self.transaction.amount, 100)
        self.assertEqual(self.transaction.balance, 150)
        self.assertEqual(self.transaction.date, time.strftime("%d/%m/%Y"))
