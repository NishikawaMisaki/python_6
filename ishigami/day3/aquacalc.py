import sys
args = sys.argv

import datetime

day = args[1]
adult = int(args[2])
child = int(args[3])

workday_adult = 2000
workday_child = 1200
sat_sun_adult = 2400
sat_sun_child = 1500

sum = 0

year = day[0:4]
month = day[4:6]
day = day[6:]

today = datetime.date(int(year),int(month),int(day))
today = int(today.strftime("%w"))

if today == 0 or today == 6:
    sum = sat_sun_adult * adult + sat_sun_child * child
else:
    sum = workday_adult * adult + workday_child * child

print(sum,end="")
