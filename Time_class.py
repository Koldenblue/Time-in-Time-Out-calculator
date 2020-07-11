class Time:

    def __init__ (self, hours=0, minutes=0, pm=False):
        '''A time object that corresponds to a 12-hour clock time.'''
        self.hours = hours
        self.minutes = minutes
        self.pm = pm
        self.pm_to_24()

    def clock_time_12(self):
        ''' Convert to 12 hour clock time.'''
        self.to_hours()
        if self.hours > 12:
            self.hours -= 12
            self.pm = True
        if self.hours == 12:
            self.pm = True

    def pm_to_24(self):
        '''If pm, convert to 24 hour time.'''
        if self.pm == True:
            if self.hours < 12:
                self.hours += 12
            self.pm = False
        # Account for 12am. Will have to put in condition if time_out < time_in, that means someone stayed past midnight.
        if self.pm == False:
            if self.hours == 12:
                self.hours = 0

    def to_minutes(self):
        '''Converts time object to only minutes.'''
        converted_minutes = self.hours * 60
        self.hours = 0
        self.minutes += converted_minutes

    def to_hours(self):
        '''Converts time object to hours, with the remainder as minutes.'''
        converted_hours = self.minutes // 60
        remaining_minutes = self.minutes % 60
        self.hours += converted_hours
        self.minutes = remaining_minutes

    def __str__(self):
        '''String in everyday 12 hour time format'''
        self.clock_time_12()
        if self.pm:
            pm_string = ' pm'
        else:
            pm_string = ''
        return (str(self.hours) + ":" + str(self.minutes) + f"{pm_string}")

myTime = Time(10, 20, True)

myTime.to_minutes()
print(myTime.minutes, 'minutes')
print(myTime.hours, 'hours')

myTime.to_hours()
print(myTime.minutes, 'minutes')
print(myTime.hours, 'hours')

print(myTime)
