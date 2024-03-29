import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        input = "stringlengtH-14"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "stringlengtH_15"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        input = "stringlengtH__16"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        input = "stringlength__----_21"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test5(self):
        input = "NOLOWERCASE"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        input = "nouppercase"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test7(self):
        input = "noDigitinpwd"
        self.assertFalse(check_pwd(input))
    
    def test8(self):
        input = "noSymbolinpwd1"
        self.assertFalse(check_pwd(input))


if __name__ == '__main__':
    unittest.main()
    
