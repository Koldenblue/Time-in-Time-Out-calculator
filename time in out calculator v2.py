
def get_time_object(time):
    pm = False
    # If user entered 'p' or 'pm', remove the characters and set the pm bool to True
    if 'pm' in time:
        pm = True
        time = time[:-2]
    elif 'p' in time_in:
        pm = True
        time = time[:-1]

    # Split input into a list with two indices: time_list[0] == hours, and time_list[1] == minutes:
    if ':' in time:
        time_list = time.split(':')
    else:
        time_list = time.split()
    
    # Convert the list items to integers:
    for t in range(len(time_list)):
        time_list[t] = int(time_list[t])

    return (Time(time_list[0], time_list[1], pm))


# Loop to get times in, out, and lunch.
while True:
    print(colored('\n-----\nHELLO', 'green'))
    timeRegex = re.compile(r'[1|2]?\d[:|\s][0|1|2|3|4|5]\d[p|pm]?$') # $ specifies that the match must occur at the end of searched text. 
    
    # First get time clocked in and out, and whether 30 min is taken off for lunch.
    print(colored("""Time in? Format 'X:YY' or 'X YY' for am, and X:YYp or 'X YYp' for pm.""", 'blue'))
    print(colored('Type \'q\' if done entering times.', 'blue'))
    #print(colored('Remember to type \'p\' for PM!!! Type \'undo\' if you have made a mistake and would like to start back at Time In entry.', 'blue'))
    # ADD IN UNDO FUNCTION
    
    time_in = input()

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