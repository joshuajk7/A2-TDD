import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        input = "stringlength14"
        expected = 14
        self.assertTrue(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
    
