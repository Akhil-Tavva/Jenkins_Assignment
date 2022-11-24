import unittest

from gcd import gcd

class TestGCD(unittest.TestCase):
    def test_gcd1(self):
        result1 = gcd(8,4)
        self.assertEqual(result1,4)
    def test_gcd2(self):
        result1 = gcd(12,24)
        self.assertEqual(result1,12)
    def test_gcd3(self):
        result1 = gcd(16,36)
        self.assertEqual(result1,4)
    def test_gcd4(self):
        result1 = gcd(10,5)
        self.assertEqual(result1,10)
    def test_gcd5(self):
        result1 = gcd(15,25)
        self.assertEqual(result1,10)

if __name__ == "__main__":
    unittest.main()
