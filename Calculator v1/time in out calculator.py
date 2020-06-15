import re
from colorama import init, Fore, Back, Style
from termcolor import colored
init()
'''first_name = input("Employee first name?")
last_name = input('Employee last name?')
start_date = input('Start Date?')
end_date = input('End Date?')'''

time_in_list = []
time_out_list = []
lunch_list = []
total_time_list = []



def calculate_hours(time_in, time_out, lunchtime): 
    
    time_in_pm = False
    # If user entered 'p' or 'pm', remove the characters and set the time_in_pm bool to True
    if 'pm' in time_in:
        time_in_pm = True
        time_in = time_in[:-2]
    elif 'p' in time_in:
        time_in_pm = True
        time_in = time_in[:-1]

    # Split input into a list with two indices: time_in_list[0] == hours, and time_in_list[1] == minutes:
    if ':' in time_in:
        time_in_list = time_in.split(':')
    else:
        time_in_list = time_in.split()
    
    # Convert the list items to integers:
    for time in range(len(time_in_list)):
        time_in_list[time] = int(time_in_list[time])

    # Similarly for time_out
    time_out_pm = False
    if 'p' in time_out:
        time_out_pm = True
        time_out = time_out[:-1]
    if ':' in time_out:
        time_out_list = time_out.split(':')
    else:
        time_out_list = time_out.split()
    # Convert to ints:
    for time in range(len(time_out_list)):
        time_out_list[time] = int(time_out_list[time])

    # If pm, add 12 hours to hour total.
    if time_in_pm == True and time_in_list[0] <= 12:
        time_in_list[0] += 12
    total_min_in = time_in_list[0] * 60 + time_in_list[1]

    # Repeat this process for time_out_list
    if time_out_pm == True and time_out_list[0] <= 12:
        time_out_list[0] += 12
    total_min_out = time_out_list[0] * 60 + time_out_list[1]
    total_time = total_min_out - total_min_in
    if lunchtime == True:
        total_time -= 30
    return total_time

# Loop to get times in, out, and lunch.
while True:
    print(colored('\n-----\nHELLO', 'green'))
    # Why is $ needed, but not ^?
    timeRegex = re.compile(r'[1|2]?\d[:|\s][0|1|2|3|4|5]\dp?$') # $ specifies that the match must occur at the end of searched text. 
    # First get time clocked in and out, and whether 30 min is taken off for lunch.
    print(colored("""Time in? Format 'X:YY' or 'X YY' for am, and X:YYp or 'X YYp' for pm.""", 'blue'))
    print(colored('Type \'q\' if done entering times.', 'blue'))
    print(colored('Remember to type \'p\' for PM!!! Type \'undo\' if you have made a mistake and would like to start back at Time In entry.', 'blue'))
    # ADD IN UNDO FUNCTION
    
    time_in = input()
    # Type in 'q' to quit out of the while loop.
    if time_in.lower() == 'q':
        break
    # Make sure the time entered is in a valid format. If not, restart loop.
    # Using the .match() method instead of the .search() method will make sure the beginning of the string time_in matches the regex!
    mo = timeRegex.match(time_in)
    if mo == None:
        print("Invalid time format! Print X:YY, or X:YYp. E.g. 12:30p")
        continue
    
    print(colored("Time out? Format 'X:YY' for am, and X:YYp for pm.", 'magenta'))
    print(colored('Remember to type \'p\' for PM!!! Type \'undo\' if you have made a mistake and would like to start back at Time In entry.', 'magenta'))
    time_out = input()
    mo = timeRegex.match(time_out)
    if mo == None:
        print("Invalid time format! Print X:YY, or X:YYp. E.g. 12:30p")
        continue

    # Get whether lunch was taken.
    while True:
        lunch = input("Lunch? y/n\n")
        if lunch.lower() == 'y':
            lunchtime = True
            break
        elif lunch.lower() == 'n':
            lunchtime = False
            break
        else:
            print("Must answer either 'y' or 'n'!")
            continue
    time_in_list.append(time_in)
    time_out_list.append(time_out)
    lunch_list.append(lunchtime)
    total_time_list.append(calculate_hours(time_in, time_out, lunchtime))



# print('Employee: ' + )
layout = '{0:<12}{1:<12}{2:<12}{3:<12}'
print(layout.format('Time in', 'Time Out', 'Lunch', 'Total time'))

for i in range(len(time_in_list)):
    print(layout.format(time_in_list[i], time_out_list[i], lunch_list[i], total_time_list[i]))



    #TODO: calculate total time in hours, format chart hours, add lunch time, employee name input, chart formatting and printing, save to file
    # possibly add in code to make sure time out > time in
    #Upload to github
    #undo function?