import unittest

def sum_pair(x, y):
    return x + y 

def lower(message):
    return message.lower()

class PracticeUnitTests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_pair(2, 2), 4)

    def test_lower(self):
        self.assertEqual(lower("BOB"), "bob")        
        
if __name__ == "__main__":
    unittest.main()