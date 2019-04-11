import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("Missouri", 43, 43)
        self.assertEqual(repr(loc2), "Location('Missouri', 43, 43)")
        loc3 = Location("San Jose", 43, 43)
        self.assertNotEqual(repr(loc3), "Location('SLO', 43, 43)") 
        self.assertEqual(repr(loc3), "Location('San Jose', 43, 43)")
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
