import unittest
from cron_obj import CronObject
from unittest.mock import patch


class TestCronObject(unittest.TestCase):
    def setUp(self):
        self.cron = CronObject()

    @patch('validator.Validator.is_step')
    def test_get_minute_with_step_returns_factored_list(self, mock_get_min):
        mock_get_min.return_value = True
        self.assertEqual(self.cron.get_cron_value('*/15', 'min'), [0, 15, 30, 45])


    @patch('validator.Validator.is_step')
    def test_get_minute_without_step_returns_full_list(self, mock_get_min):
        mock_get_min.return_value = False
        self.assertEqual(self.cron.get_cron_value('*', 'min'), list(range(60)))

    def test_get_minute_from_range(self):
        self.assertEqual(self.cron.get_cron_value('3-5', 'min'), [3, 4, 5])

    def test_get_minute_specific_number(self):
        x = self.cron.get_cron_value('50', 'min')
        self.assertEqual(x, [50])

    def test_get_day_from_list(self):
        self.assertEqual(self.cron.get_cron_value('1,15', 'day'), [1, 15])


if __name__ == '__main__':
    unittest.main()
