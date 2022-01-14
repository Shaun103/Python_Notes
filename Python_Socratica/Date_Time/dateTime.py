import datetime

max = datetime.date(9999, 12, 31)
min = datetime.timedelta(1)

gvr = datetime.date(1956, 1, 31)  

print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

dir(datetime)

mill = datetime.date(2000, 1, 1) # yyyy - mm -- dd
dt = datetime.timedelta(100)
print(mill + dt) # prints 100 days after previous date

print(gvr.strftime("%A, %B %d, %Y"))

# more modern way
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)

print(launch_time)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

print(launch_datetime)

now = datetime.datetime.today()
print(now)
print(now.microsecond)

moon_landing = "7/20/1969"

moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime))
