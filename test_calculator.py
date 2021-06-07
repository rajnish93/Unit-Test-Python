import unittest
import calculator

class TestCal(unittest.TestCase):
    ## Test Add Function
    def test_add(self):
        result = calculator.add(30,15)
        self.assertEqual(result,45)
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
