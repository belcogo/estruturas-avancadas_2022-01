import unittest
from GA2_Q1 import findKthElement

class TestKthElement(unittest.TestCase):
  def setUp(self): 
    self.array = list[int]
    self.array = [3, 1, 9, 12, 4, 8, 6, 5]

  def test_invalid_input_1(self):
    value = findKthElement(self.array, -1)
    expected = -1
    self.assertEqual(value, expected) 
  
  def test_invalid_input_0(self):
    value = findKthElement(self.array, 0)
    expected = -1
    self.assertEqual(value, expected)

  def test_invalid_input_8(self):
    value = findKthElement(self.array, -1)
    expected = -1
    self.assertEqual(value, expected) 

  def test_valid_input_1(self):
    value = findKthElement(self.array, 1)
    expected = 12
    self.assertEqual(value, expected) 

  def test_valid_input_3(self):
    value = findKthElement(self.array, 3)
    expected = 8
    self.assertEqual(value, expected) 

  def test_valid_input_6(self):
    value = findKthElement(self.array, 6)
    expected = 4
    self.assertEqual(value, expected)

if __name__ == '__main__':
    unittest.main()