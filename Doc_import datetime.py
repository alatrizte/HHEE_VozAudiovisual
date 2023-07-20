import datetime

# Starts with knowing the day of the week
week_day=datetime.datetime.now().isocalendar()[2]

# Calculates Starting date (Sunday) for this case by subtracting current date with time delta of the day of the week
start_date=datetime.datetime.now() - datetime.timedelta(days=week_day-1)
print(datetime.timedelta(days=week_day))

# Prints the list of dates in a current week
dates=[str((start_date + datetime.timedelta(days=i)).date()) for i in range(5)]
print(dates)