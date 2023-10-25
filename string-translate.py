""" 
Tags:
ascii alphabet
string translate
letter mapping
letter mask
"""

import string
import unittest

def caesar(plain_text, shift_num=1):
    """
    Make a cipher of the text by shifting the letters n place in the alphabet 
    """
    
    # generates a string with all lower case letters in the alphabet 'abcdefghijklmnopqrstuvwxyz'
    letters = string.ascii_lowercase 
    
    # create a mask by changing the starting place in the alphabet and looping around
    mask = letters[shift_num:] + letters[:shift_num]
    
    # make the translation mapping using the mapping between original alphanet and shifted alphabet
    trantab = str.maketrans(letters, mask)
    
    # apply the translation
    return plain_text.translate(trantab)


class CaesarTestCase(unittest.TestCase):
    def test_a(self):
        start = "aaa"
        result = caesar(start, 1)
        self.assertEqual(result, "bbb")
        result = caesar(start, 5)
        self.assertEqual(result, "fff")

    def test_punctuation(self):
        start = "aaa.bbb"
        result = caesar(start, 1)
        self.assertEqual(result, "bbb.ccc")
        result = caesar(start, -1)
        self.assertEqual(result, "zzz.aaa")

    def test_whitespace(self):
        start = "aaa    bb b"
        result = caesar(start, 1)
        self.assertEqual(result, "bbb    cc c")
        result = caesar(start, 3)
        self.assertEqual(result, "ddd    ee e")

    def test_wraparound(self):
        start = "abc"
        result = caesar(start, -1)
        self.assertEqual(result, "zab")
        result = caesar(start, -2)
        self.assertEqual(result, "yza")
        result = caesar(start, -3)
        self.assertEqual(result, "xyz")

        start = "xyz"
        result = caesar(start, 1)
        self.assertEqual(result, "yza")
        result = caesar(start, 2)
        self.assertEqual(result, "zab")
        result = caesar(start, 3)
        self.assertEqual(result, "abc")


if __name__ == "__main__":
    unittest.main()