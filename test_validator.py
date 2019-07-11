import unittest
from validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_is_step(self):
        self.assertEqual(bool(self.validator.is_step('*/15')), True)
        self.assertEqual(bool(self.validator.is_step('*/2')), True)
        self.assertEqual(bool(self.is_step('*')), False)

    def test_is_range(self):
        self.assertEqual(bool(self.validator.is_range('1-5')), True)
        self.assertEqual(bool(self.validator.is_range('1')), False)
        self.assertEqual(bool(self.validator.is_range('1,2,3')), False)

    def test_is_list(self):
        self.assertEqual(bool(self.validator.is_list('1,5')), True)
        self.assertEqual(bool(self.validator.is_list('1,5,8')), True)





if __name__ == '__main__':
    unittest.main()
