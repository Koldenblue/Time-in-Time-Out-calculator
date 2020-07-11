import re
from colorama import init, Fore, Back, Style
from termcolor import colored
from Time_class import Time
init()
from Timesheet_class import Timesheet

def main():
    print(colored('\n-----\nHELLO', 'green'))
    current_timesheet = Timesheet()
    current_timesheet.get_time_object()


# Loop to get times in, out, and lunch.

    time_in_list.append(time_in)
    time_out_list.append(time_out)
    lunch_list.append(lunchtime)
    total_time_list.append(calculate_hours(time_in, time_out, lunchtime))

main()