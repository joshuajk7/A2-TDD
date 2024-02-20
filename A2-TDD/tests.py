import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        input = "stringlength14"
        expected = 14
        if expected == 14:
            expected = True
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "stringlength_15"
        expected = 15
        if expected == 15:
            expected = True
        self.assertEqual(check_pwd(input), expected)

if __name__ == '__main__':
    unittest.main()
    
