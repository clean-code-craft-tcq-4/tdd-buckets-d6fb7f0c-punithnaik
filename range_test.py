import unittest
import range
from unittest.mock import patch 


class Test(unittest.TestCase):
  def test_simple(self):
    self.assertTrue(range.check_range([4,5]) == '4-5,2')
    
if __name__ == '__main__':
  unittest.main()
