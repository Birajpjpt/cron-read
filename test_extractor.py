import unittest
from extractor import Extractor


class TestExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor()

    def test_extract_step_values_for_minutes_expr(self):
        self.assertEqual(self.extractor.extract_step_values('*/15', 'min'), [0, 15, 30, 45])
        self.assertEqual(self.extractor.extract_step_values('*/20', 'min'), [0, 20, 40])

    def test_extract_step_values_for_hour_expr(self):
        self.assertEqual(self.extractor.extract_step_values('*/12', 'hour'), [0, 12])
        self.assertEqual(self.extractor.extract_step_values('*/6', 'hour'), [0, 6, 12, 18])

    def test_extract_step_values_for_day_expr(self):
        self.assertEqual(self.extractor.extract_step_values('*/5', 'day'), [1, 6, 11, 16, 21, 26, 31])
        self.assertEqual(self.extractor.extract_step_values('*/10', 'day'), [1, 11, 21, 31])

    def test_extract_step_values_for_month_expr(self):
        self.assertEqual(self.extractor.extract_step_values('*/2', 'month'), [1, 3, 5, 7, 9, 11])
        self.assertEqual(self.extractor.extract_step_values('*/10', 'month'), [1, 11])

    def test_extract_step_values_for_dow_expr(self):
        self.assertEqual(self.extractor.extract_step_values('*/2', 'dow'), [1, 3, 5, 7])
        self.assertEqual(self.extractor.extract_step_values('*/7', 'dow'), [1])

    def test_extract_range_values_expr(self):
        self.assertEqual(self.extractor.extract_range_values('57-59', 'min'), [57, 58, 59])
        self.assertEqual(self.extractor.extract_range_values('0-4', 'hour'), [0, 1, 2, 3, 4])

    def test_extract_range_values_for_error(self):
        self.assertEqual(self.extractor.extract_range_values('57-69', 'min'), "Error")
        self.assertEqual(self.extractor.extract_range_values('12-9', 'hour'), "Error")

    def test_extract_specific_num_expr(self):
        self.assertEqual(self.extractor.extract_specific_num('59', 'min'), [59])
        self.assertEqual(self.extractor.extract_specific_num('25', 'hour'), "Error")
        self.assertEqual(self.extractor.extract_specific_num('0', 'day'), "Error")

    def test_extract_list_obj_expr(self):
        self.assertEqual(self.extractor.extract_list_obj('1,5,25', 'min'), [1, 5, 25])
        self.assertEqual(self.extractor.extract_list_obj('1,15', 'day'), [1, 15])
        self.assertEqual(self.extractor.extract_list_obj('2,24', 'hour'), "Error")
        self.assertEqual(self.extractor.extract_list_obj('0,8', 'day'), "Error")

    def test_extract_specific_num(self):
        self.assertEqual(self.extractor.extract_list_obj('0', 'hour'), [0])

    def test_extract_all_values(self):
        self.assertEqual(self.extractor.extract_all_values('dow'), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.extractor.extract_all_values('hour'), list(range(0, 24)))


if __name__ == '__main__':
    unittest.main()
