import unittest
import calculator

class TestCal(unittest.TestCase):
    ## Test Add Function
    def test_add(self):
        # result = calculator.add(30,15)
        # self.assertEqual(result,45)
        self.assertEqual(calculator.add(30,15),45)
        self.assertEqual(calculator.add(30,-15),15)
        self.assertEqual(calculator.add(-30,-15),-45)
        self.assertEqual(calculator.add(-30,15),-15)
    ## Test Subtract Function
    def test_sub(self):
        result = calculator.sub(30,15)
        self.assertEqual(result,15)
    ## Test Multiplication Function
    def test_mul(self):
        result = calculator.mul(30,15)
        self.assertEqual(result,450)
    ## Test Division Function
    def test_div(self):
        result = calculator.div(30,15)
        self.assertEqual(result,2)
"""
 Run code using:
 python -m unittest test_calculator.py
 """
if __name__=='__main__':
    unittest.main()
"""
 Run code using if main is present:
 python test_calculator.py
 """