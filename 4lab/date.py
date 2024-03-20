#1
import datetime
x = datetime.datetime.now() - datetime.timedelta(5)
print(x)
#2
yest = datetime.datetime.now() - datetime.timedelta(1)
tod = datetime.datetime.now()
tom = datetime.datetime.now() + datetime.timedelta(1)
print("Yesterday:", yest)
print("Today:", tod)
print("Tomorrow:", tom)
#3
x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M:%S"))
#4
from datetime import datetime, time
date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
date2 = datetime.now()
difference = (date2 - date1).total_seconds()
print(difference)
