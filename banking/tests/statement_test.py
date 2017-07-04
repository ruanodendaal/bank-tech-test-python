import unittest
from statement import Statement

class TestStatement(unittest.TestCase):

    def setUp(self):
        self.statement = Statement()

    def test_default_options_set(self):
        self.assertEqual(self.statement.summary, [])
