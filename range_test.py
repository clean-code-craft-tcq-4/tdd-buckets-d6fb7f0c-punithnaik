import unittest
from range import bucket_amperes, bucket_individual_readings, report_consecutive_groups, check_error, input_to_amps

class TestAmperesRanges(unittest.TestCase):
    def test_two_values_are_reported_in_range(self):
        self.assertEqual(bucket_amperes([4, 5]), '4-5, 2')
        
    def test_individual_bucketing(self):
        expected_ampere_counts = [
            {'amp': 0, 'count': 0},
            {'amp': 1, 'count': 0},
            {'amp': 2, 'count': 2},
            {'amp': 3, 'count': 0},
            {'amp': 4, 'count': 1},
            {'amp': 5, 'count': 1},
        ]
        self.assertEqual(bucket_individual_readings([5, 2, 4, 2]), expected_ampere_counts)

    def test_consecutive_grouping(self):
        self.assertEqual(report_consecutive_groups([0, 0, 2, 0, 1, 1]), [[2], [1, 1]])

    #------------Current Sensing test code----------------
    def test_check_error(self):
      self.assertEqual(remove_error([0,10,100,1000,4000,4095]),[0,10,100,1000,4000])

    def test_input_to_amps(self):
      self.assertEqual(input_to_amps(0),0)
      self.assertEqual(input_to_amps(400),1)
      self.assertEqual(input_to_amps(800),2)
      self.assertEqual(input_to_amps(1200),3)
      self.assertEqual(input_to_amps(1600),4)
      self.assertEqual(input_to_amps(2000),5)
      self.assertEqual(input_to_amps(2400),6)
      self.assertEqual(input_to_amps(2800),7)
      self.assertEqual(input_to_amps(3200),8)
      self.assertEqual(input_to_amps(3600),9)
      self.assertEqual(input_to_amps(4000),10)
      self.assertEqual(input_to_amps(4094),10)
      
unittest.main()
