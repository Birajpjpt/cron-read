from validator import Validator
from extractor import Extractor


class CronObject:

    def __init__(self):
        self.validator = Validator()
        self.extractor = Extractor()

    def get_cron_value(self, expr, time_unit):
        """valid time units (min, hour, day, month, dow)"""
        if '*' in expr:
            if self.validator.is_step(expr):
                return self.extractor.extract_step_values(expr, time_unit)
            else:
                return self.extractor.extract_all_values(time_unit)

        if '-' in expr and self.validator.is_range(expr):
            return self.extractor.extract_range_values(expr, time_unit)

        if ',' in expr and self.validator.is_list(expr):
            return self.extractor.extract_list_obj(expr, time_unit)

        if expr.isdigit():
            return self.extractor.extract_specific_num(expr, time_unit)
        else:
            return "Error"
