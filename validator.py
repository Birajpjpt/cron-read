import re


class Validator:

    def is_step(self, expr):
        return bool(re.match(r"\*\/\d{1,2}", expr))

    def is_range(self, expr):
        return bool(re.match(r"\d-\d{1,2}", expr))

    def is_list(self, expr):
        return bool(re.match(r"\d+(,\d+)*", expr))