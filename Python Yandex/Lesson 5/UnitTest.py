import unittest

def main():
    pass

class TestFactorial(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorial(1),1)
    def test_2(self):
        self.assertEqual(factorial(5),120)

unittest.main()