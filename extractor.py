class Extractor:
    time_unit_max = {'min': 60, 'hour': 24, 'day': 31, 'month': 12, 'dow': 7}

    def extract_step_values(self, expr, time_unit):
        """expr should be something like */5, valid time units (min, hour, day, month, dow)"""
        extracted_value = []

        divisor = int(expr.split('/')[1])
        factor = int(self.time_unit_max[time_unit] / divisor)  # To Do: handle out of range exception
        base_num = self._lower_upper_value(time_unit)[0]
        for n in range(0, factor + 1):
            extracted_value.append(base_num)
            base_num = base_num + divisor
        extracted_value = [value for value in extracted_value if value <= self._lower_upper_value(time_unit)[1]]

        return list(sorted(set(extracted_value)))

    def extract_range_values(self, expr, time_unit):
        """expr should be something like 2-7, valid time units (min, hour, day, month, dow)"""
        extracted_value = []
        l_range_val, u_range_val = int(expr.split('-')[0]), int(expr.split('-')[1])
        if (self._lower_upper_value(time_unit)[0] <= u_range_val <= self._lower_upper_value(time_unit)[1]) \
                and (self._lower_upper_value(time_unit)[0] <= l_range_val <= self._lower_upper_value(time_unit)[1]) \
                and l_range_val < u_range_val:
            for n in range(l_range_val, u_range_val + 1):
                extracted_value.append(n)
            return extracted_value
        else:
            return 'Error'

    def extract_specific_num(self, expr, time_unit):
        """expr should be an int, valid time units (min, hour, day, month, dow)"""
        extracted_value = []
        if expr.isdigit() and self._lower_upper_value(time_unit)[0] <= int(expr) <= self._lower_upper_value(time_unit)[1]:
            extracted_value.append(int(expr))
            return extracted_value
        else:
            return 'Error'

    def extract_list_obj(self, expr, time_unit):
        """expr should be an comma separated value, valid time units (min, hour, day, month, dow)"""
        expr_list = [int(a) for a in expr.split(',')]
        l_range, r_range = self._lower_upper_value(time_unit)[0], self._lower_upper_value(time_unit)[1]
        valid_time_value = list(range(l_range, r_range + 1))
        if all(x in valid_time_value for x in expr_list):
            return list(sorted(set(expr_list)))
        else:
            return 'Error'

    def extract_all_values(self, time_unit):
        """expr should be *, valid time units (min, hour, day, month, dow)"""
        extracted_value = list(range(self._lower_upper_value(time_unit)[0], self._lower_upper_value(time_unit)[1] + 1))
        return extracted_value

    def _lower_upper_value(self, time_unit):
        if time_unit in ['min', 'hour']:
            return 0, self.time_unit_max[time_unit] - 1
        else:
            return 1, self.time_unit_max[time_unit]
