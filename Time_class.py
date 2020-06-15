class Time:

    def __init__ (self, hours=0, minutes=0, pm=False):
        self.hours = hours
        self.minutes = minutes
        self.pm = pm

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
        '''Converts time to only minutes.'''
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
        return str(myTime.hours) + " hours " + str(myTime.minutes) + " minutes"

    def

myTime = Time(10, 20)
myTime.to_minutes()
print(myTime.minutes)
print(myTime.hours)

myTime.to_hours()
print(myTime)