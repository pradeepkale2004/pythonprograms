import calendar
year = int(input('Enter the year of calender'))
month = int(input('Enter the month of the year'))

monthh =calendar.month(year,month)
print(monthh)