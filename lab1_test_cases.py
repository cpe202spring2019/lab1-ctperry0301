import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Protects against a non list"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """Checks to see if the max is 5 if there are 2 or more of the max"""
        self.assertEqual(max_list_iter([4, 5, 4, 3, 2, 1, 5, 1] ), 5)
        """Returns max value while checking for negatives"""
        self.assertEqual(max_list_iter([-4, -3, -2, -1, -10]), -1)
        """ Returns max value if there is only 1 max value"""
        self.assertEqual(max_list_iter([4, 4]), 4)
        """Returns None type if list is empty"""
        self.assertEqual(max_list_iter([]), None)
   
    
    def test_reverse_rec(self):
        """Returns a basic reversed list, """
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        """Protects against a non list"""
        with self.assertRaises(ValueError):
            reverse_rec(None)
        """Returns list if len(int_list) <= 1, no need to reverse. """
        self.assertEqual(reverse_rec([1]), [1])
        """Returns list given only 2 elements, makes sure reverse bounds dont
        return an outOfRangeError for the list """
        self.assertEqual(reverse_rec([0, 1]), [1, 0])
   
    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, []), None)
        with self.assertRaises(ValueError):
            bin_search(1, 0, 1, None)
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 7)
        self.assertEqual(bin_search(7, 3, 2, list_val), None)
if __name__ == "__main__":
        unittest.main()

    
