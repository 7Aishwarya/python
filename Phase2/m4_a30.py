import unittest
from m4_a30_2 import getDiscount 
 
class TestDiscount(unittest.TestCase):
    def test_discount(self):
        self.assertAlmostEqual(getDiscount(55), 0)
        self.assertAlmostEqual(getDiscount(60), 15)
        self.assertAlmostEqual(getDiscount(65), 15)
        self.assertAlmostEqual(getDiscount(68), 15)
        self.assertAlmostEqual(getDiscount(70), 30)
        self.assertAlmostEqual(getDiscount(75), 30)
