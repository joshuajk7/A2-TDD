import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        input = "stringlength14"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "stringlength_15"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        input = "stringlength__16"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        input = "stringlength__----_21"
        expected = False
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
    
