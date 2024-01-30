from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(5, 10, '+')
        self.assertEqual(15, result)

    def test_minus(self):
        result = operations(15, 5, '-')
        self.assertEqual(10, result)

    def test_multiply(self):
        result = operations(15, 5, '*')
        self.assertEqual(75, result)
