import calendar
import datetime
import time


print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.month(2019,10))
print(calendar.monthcalendar(2019,10))
print(calendar.calendar(2019))

day_of_the_week = calendar.weekday(2019, 3, 8 )
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)

how_many_leap_days = calendar.leapdays(2020,2080)
print(how_many_leap_days)