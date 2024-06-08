import datetime

#curr date
now = datetime.datetime.now()
print(now)

#format date
x = now.strftime("%A, %m %d, %Y - %H:%m")
print(x)

#weekdays
print(now.strftime("%A, %a, %w, %u"))

#month
print(now.strftime("%B, %b, %m"))

#year
print(now.strftime("%Y, %y"))

#time 24hr
print(now.strftime("%H:%M"))

#time AM/PM
print(now.strftime("%I:%M %p"))

#timezone
print(now.strftime("%Z"))

#day of year / week of year / century
print(now.strftime("%j %U %W %C"))

#local date
print(now.strftime("%c"))

#datediff num days between dates
from datetime import date
start = date(2023, 7, 29)
end = date(2024, 3, 22)
delta = end - start
print(delta)
print(delta.days)

#print calendar
import calendar
print(calendar.month(2023,4))