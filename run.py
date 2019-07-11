import sys
from cron_obj import CronObject
from crontab import CronSlices

if __name__ == "__main__":

    if len(sys.argv) != 3:
            print("Invalid Number of argument")

    if len(sys.argv) == 3:
        cron_obj = CronObject()
        command = sys.argv[2]
        cron_expr = sys.argv[1]
        if not CronSlices.is_valid(cron_expr):
            sys.exit('Invalid Cron Expression')
        time_field_list = cron_expr.split(' ')
        mins_list = cron_obj.get_min(time_field_list[0])
        hour_list = cron_obj.get_hour(time_field_list[1])
        day_list = cron_obj.get_day(time_field_list[2])
        month_list = cron_obj.get_month(time_field_list[3])
        dow_list = cron_obj.get_dow(time_field_list[4])

        min_field = "minutes".ljust(14)
        hr_field = "hour".ljust(14)
        dom_field = "day of month".ljust(14)
        mon_field = "month".ljust(14)
        dow_field = "day of week".ljust(14)
        cmd_field = "command".ljust(14)

        print(f'{min_field}{" ".join(map(str, mins_list))}'
              f'\n{hr_field}{" ".join(map(str, hour_list))}'
              f'\n{dom_field}{" ".join(map(str, day_list))}'
              f'\n{mon_field}{" ".join(map(str, month_list))}'
              f'\n{dow_field}{" ".join(map(str, dow_list))}'
              f'\n{cmd_field}{command}')



