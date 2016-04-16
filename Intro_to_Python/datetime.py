# datetime

# time
import datetime

t = datetime.time(4, 20, 1)

print t
print 'hour: ', t.hour
print 'minute: ', t.minute
print 'second: ', t.second
print 'microsecond: ', t.microsecond
print 'tzinfo: ', t.tzinfo

# check min and max values a time of day can have
print 'Earliest: ', datetime.time.min
print 'Latest: ', datetime.time.max
print 'Resolution: ', datetime.time.resolution


# dates
today = datetime.date.today()
another_day = datetime.date(2015,01,02)

print today
print another_day

print 'ctime: ', today.ctime()
print 'tuple: ', today.timetuple()
print 'ordinal: ', today.toordinal()
print 'Year: ', today.year
print 'Month: ', today.month
print 'Day: ', today.day

print 'Earliest: ', datetime.date.min
print 'Latest: ', datetime.date.max
print 'Resolution:', datetime.date.resolution

# use replace to create new dates
d1 = datetime.date(2015, 3, 11)
print 'd1:', d1

d2 = d1.replace(year = 2014, month = 2, day = 1)
print 'd2:', d2


# arithmetic with dates
d1

d2

x = d1 - d2
type(x.days)

