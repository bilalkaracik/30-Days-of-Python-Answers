#Day 16
from datetime import datetime
#1
now = datetime.now()
day = now.day
print(day)
month = now.month
month
year = now.year
year
hour = now.hour
hour
minute = now.minute
minute
timestamp =now.timestamp()
timestamp

#2
now = datetime.now()
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print('t :', t   )

#3
date_string = "5 December, 2019"
print("Date String =" , date_string)

#4
from datetime import date
t = date(year= 2023, month= 2, day=18)
new_year = date(year=2024, month=2, day=18)
difference = new_year - t
difference

#5
before = date(1970, 1, 1)
now = date(2023, 2, 23)
diff = now - before
diff

















