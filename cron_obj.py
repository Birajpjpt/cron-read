from validator import Validator
from extractor import Extractor


class CronObject:

    def __init__(self):
        self.validator = Validator()
        self.extractor = Extractor()

    def get_min(self, min_expr):
        if '*' in min_expr:
            if self.validator.is_step(min_expr):
                return self.extractor.extract_step_values(min_expr, 'min')
            else:
                return list(range(60))

        if '-' in min_expr and self.validator.is_range(min_expr):
            return self.extractor.extract_range_values(min_expr, 'min')

        if ',' in min_expr and self.validator.is_range(min_expr):
            return self.extractor.extract_list_obj(min_expr, 'min')

        if min_expr.isdigit():
            return self.extractor.extract_specific_num(min_expr, 'min')

        else:
            return "Error"

    def get_hour(self, hour_expr):
        if '*' in hour_expr:
            if self.validator.is_step(hour_expr):
                return self.extractor.extract_step_values(hour_expr, 'hour')
            else:
                return list(range(24))

        if '-' in hour_expr and self.validator.is_range(hour_expr):
            return self.extractor.extract_range_values(hour_expr, 'hour')

        if ',' in hour_expr and self.validator.is_range(hour_expr):
            return self.extractor.extract_list_obj(hour_expr, 'hour')

        if hour_expr.isdigit():
            return self.extractor.extract_specific_num(hour_expr, 'hour')

        else:
            return "Error"

    def get_month(self, month_expr):
        if '*' in month_expr:
            if self.validator.is_step(month_expr):
                return self.extractor.extract_step_values(month_expr, 'month')
            else:
                return list(range(1, 13))

        if '-' in month_expr and self.validator.is_range(month_expr):
            return self.extractor.extract_range_values(month_expr, 'month')

        if ',' in month_expr and self.validator.is_range(month_expr):
            return self.extractor.extract_list_obj(month_expr, 'month')

        if month_expr.isdigit():
            return self.extractor.extract_specific_num(month_expr, 'month')

        else:
            return "Error"

    def get_day(self, day_expr):
        if '*' in day_expr:
            if self.validator.is_step(day_expr):
                return self.extractor.extract_step_values(day_expr, 'day')
            else:
                return list(range(1, 32))

        if '-' in day_expr and self.validator.is_range(day_expr):
            return self.extractor.extract_range_values(day_expr, 'day')

        if ',' in day_expr and self.validator.is_list(day_expr):
            return self.extractor.extract_list_obj(day_expr, 'day')

        if day_expr.isdigit():
            return self.extractor.extract_specific_num(day_expr, 'day')

        else:
            return "Error"

    def get_dow(self, dow_expr):
        if '*' in dow_expr:
            if self.validator.is_step(dow_expr):
                return self.extractor.extract_step_values(dow_expr, 'dow')
            else:
                return list(range(1, 8))

        if '-' in dow_expr and self.validator.is_range(dow_expr):
            return self.extractor.extract_range_values(dow_expr, 'dow')

        if ',' in dow_expr and self.validator.is_range(dow_expr):
            return self.extractor.extract_list_obj(dow_expr, 'dow')

        if dow_expr.isdigit():
            return self.extractor.extract_specific_num(dow_expr, 'dow')

        else:
            return "Error"