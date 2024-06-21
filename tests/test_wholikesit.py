import sys
import os
current_dir = os.getcwd()
sys.path.append("/home/user/python-exercises/")
import unittest

import wholikesit

# test wholikesit.py
class Test(unittest.TestCase):
    def test0_numlikes(self):
        print("test wholikesit")
        self.assertEqual(wholikesit.numlikes([]), 'no one likes this')
        self.assertEqual(wholikesit.numlikes(['Peter']), 'Peter likes this')
        self.assertEqual(wholikesit.numlikes(['Jacob', 'Alex']), 'Jacob and Alex like this')
        self.assertEqual(wholikesit.numlikes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
        self.assertEqual(wholikesit.numlikes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

if __name__ == '__main__':
    unittest.main()


