import datetime
import Time_class
import re
from colorama import init, Fore, Back, Style
from termcolor import colored

class Timesheet:
    '''A timesheet containing a list of times in and out, over the course of a month, for a single employee.
    If lunch is taken, half an hour is subtracted from that day's time. The timesheet displays employee name, 
    timesheet dates, the chart of times, and the total time for the month.'''

    def __init__(self, date=datetime.datetime.now()):
        '''Constructor for a new timesheet.'''
        self.date = date

    def get_time_object(self):
        '''Gets the time in and time out for a single day.'''
        # $ specifies a match for 12 hour time.
        timeRegex = re.compile(r'^1?\d[:|\s][0-5]\d(p|pm)?$')

        while True:
            # First get time clocked in, or type 'q' to quit.
            print(colored("""Time in? Format 'X:YY' or 'X YY' for am, and X:YYp or 'X YYp' for pm.""", 'blue'))
            print(colored('Type \'q\' if done entering times.', 'blue'))
            time_in = input()
            if time_in.lower() == 'q':
                break
            # Make sure the time entered is in a valid format. If not, restart loop.
            # Using the .match() method instead of the .search() method will make sure the beginning of the string time_in matches the regex!
            mo = timeRegex.search(time_in)
            if mo == None:
                print("Invalid time format! Print X:YY, or X:YYp. E.g. 12:30p")
                continue

            # Get time out
            print(colored("Time out? Format 'X:YY' for am, and X:YYp for pm.", 'magenta'))
            print(colored('Type "undo" if you have made a mistake and would like to start back at the Time In entry.', 'magenta'))
            time_out = input()
            if time_out.lower() == 'undo':
                continue
            mo = timeRegex.search(time_out)
            if mo == None:
                print("Invalid time format! Print X:YY, or X:YYp. E.g. 12:30p")
                continue
            break

        time_in_list = self.get_time_array(time_in)
        time_out_list = self.get_time_array(time_out)

        clock_in = Time_class.Time(time_in_list[0], time_in_list[1], time_in_list[2])
        clock_out = Time_class.Time(time_out_list[0], time_out_list[1], time_out_list[2])

        print('Time in is {0}. Time out is {1}.'.format(str(clock_in), str(clock_out)))

        # Get whether lunch was taken.
        while True:
            lunch = input('Lunch? y/n\nType "undo" to start back at the input of time in.')
            if lunch.lower() == 'undo':
                continue
            if lunch.lower() == 'y':
                lunchtime = True
                break
            elif lunch.lower() == 'n':
                lunchtime = False
                break
            else:
                print("Must answer either 'y' or 'n'!")
                continue

    def get_time_array(self, time):
        '''Takes the user input, and converts it to an array with time_list[0] == hours, time_list[1] == minutes.
        time_list[2] == true if pm, false if am.'''
        # First initialize pm.
        pm = False
        # If user entered 'p' or 'pm', remove the characters and set the pm bool to True
        if 'pm' in time:
            pm = True
            time = time[:-2]
        elif 'p' in time:
            pm = True
            time = time[:-1]

        # Split input into a list with two indices: time_list[0] == hours, and time_list[1] == minutes
        # Then set time_list[2] to pm.
        if ':' in time:
            time_list = time.split(':')
            time_list.append(pm)
        else:
            time_list = time.split()
            time_list.append(pm)
        # Convert the time_list values to integers:
        for t in range(2):
            time_list[t] = int(time_list[t])

        return time_list