import unittest
from m4_a32_1 import bubbleSort
 
class test_sorting:
    def test_cases(self):
        self.assertAlmostEqual(bubbleSort([1,53,242,11,23]), [1,11,23,53,242])
        self.assertAlmostEqual(bubbleSort([0,332,123,6,4]), [4,6,123,332])
        self.assertAlmostEqual(bubbleSort([4,2,14,71,46]), [2,4,14,46,71])
