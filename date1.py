
#python data 1.

from datetime import date, timedelta
dt = date.today() - timedelta(5)
print("Current Date :", date.today())
print("5 days before Current Dste :", dt)


#python data 2.

import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days = 1)
print("Yesterday :",yesterday)
print("Today :", today)
print("Tomorrow :", tomorrow)


#python data 3.

import datetime
data = datetime.datetime.today().replace(microsecond = 0)
print()
print(data)
print()


#python data 4
from datetime import datetime,time
def different(dt2,dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime("2015-01-01 01:00:00", "%Y - %m - %d  %H:%M:&S")
date2 = datetime.now()
print("\n%d seconds" %(different(date2,date1)))
print()