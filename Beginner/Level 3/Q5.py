'''
5. Create a class 'Time' and initialize it with hours and minutes.
 Create a method addTime() which should take two Time objects and add them.

 E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min) Create another method displayTime() which should print the time.
 Also, create a method displayMinute() which should display the total minutes in the Time.
 E.g.- (1 hr 2 min) should display 62 minutes.
'''

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, t1, t2):
        total_mins =t1.minutes+t2.minutes
        hour_carry = total_mins//60
        total_mins %= 60

        total_hours = t1.hours +t2.hours +hour_carry
        return (f"{total_hours} hr and {total_mins} min")

    def displayTime(self):
        return (f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total = self.hours *60 + self.minutes
        return (f"{total} minutes")

time1 = Time(2, 50)
time2 = Time(1, 20)
print(time1.addTime(time1, time2))
print(time1.displayTime())
print(time2.displayMinute())

