import unittest

from gcd import gcd

class TestGCD(unittest.TestCase):
    def test_gcd4(self):
        result1 = gcd(10,5)
        self.assertEqual(result1,10)
    def test_gcd5(self):
        result1 = gcd(15,25)
        self.assertEqual(result1,10)

if __name__ == "__main__":
    unittest.main()
