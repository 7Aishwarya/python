import unittest
from m4_a31_1 import getDiscount
 
class Test_discount(unittest.TestCase):
    def test_all(self):
        self.assertAlmostEqual(getDiscount(55,'M'), 0)
        self.assertAlmostEqual(getDiscount(60, 'M'), 20)
        self.assertAlmostEqual(getDiscount(55, 'F'), 15)
        self.assertAlmostEqual(getDiscount(65, 'F'), 25)
