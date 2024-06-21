import sys
import os
current_dir = os.getcwd()
sys.path.append("/home/user/python-exercises/")
import unittest

import reverseword

# test reverseword.py
class Test(unittest.TestCase):
    def test0_revstr(self):
        print("test revstr")
        self.assertEqual(reverseword.revstr('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        self.assertEqual(reverseword.revstr('apple'), 'elppa')
        self.assertEqual(reverseword.revstr('a b c d'), 'a b c d')
        self.assertEqual(reverseword.revstr('double  spaced  words'), 'elbuod  decaps  sdrow')
        self.assertEqual(reverseword.revstr('stressed desserts'), 'desserts stressed')
        self.assertEqual(reverseword.revstr('hello hello'), 'olleh olleh')

"""

@test.describe('Random Tests')
def _():
    
    from random import randrange as rand, sample
    
    words = ["Kata", "should", "always", "have", "random", "tests", "case", "to", "avoid", "hardocoded", "solution.", "This", "is", "a", "rule!"]
    
    for _ in range(50):
        s = (" "*rand(1,3)).join( sample(words, rand(len(words))))
        exp = " ".join(("".join(list(s)[::-1])).split(" ")[::-1])
        @test.it(f"testing for reverse_words({s})")
        def _():
            test.assert_equals(reverse_words(s), exp)

"""

if __name__ == '__main__':
    unittest.main()