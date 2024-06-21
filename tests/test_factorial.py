import sys
import os
current_dir = os.getcwd()
sys.path.append("/home/user/python-exercises/")
import unittest

import factorial #import file to test

#test all numbers are incl
#test different types of nums decimals?
#edge cases 0, -1
#test operation is correct
#error handle for blank input null or none

# test factorial.py
class Test(unittest.TestCase):
    def test0_gimme(self):
        print("test gimme")
        self.assertEqual(factorial.gimmefactorial(0), 1)
        self.assertEqual(factorial.gimmefactorial(-1), None)
        self.assertIsNone(factorial.gimmefactorial(-1))
        self.assertEqual(factorial.gimmefactorial(1), 1)
        self.assertEqual(factorial.gimmefactorial(5), 120)
        self.assertEqual(factorial.gimmefactorial(10), 3628800)
        self.assertEqual(factorial.gimmefactorial(-4) , None)
        self.assertEqual(factorial.gimmefactorial(3), 6)

    def test1_recurse(self):
        print("test recurse")
        self.assertEqual(factorial.recursefactorial(0), 0)
        self.assertEqual(factorial.recursefactorial(-1), None)
        self.assertIsNone(factorial.recursefactorial(-1))
        self.assertEqual(factorial.recursefactorial(1), 1)
        self.assertEqual(factorial.recursefactorial(5), 120)
        self.assertEqual(factorial.recursefactorial(10), 3628800)
        self.assertEqual(factorial.recursefactorial(-4), None)
        self.assertEqual(factorial.recursefactorial(3), 6)

if __name__ == '__main__':
    unittest.main()



