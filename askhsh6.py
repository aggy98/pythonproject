import calendar



year = int(input("GIVE YEAR:"))

month = int(input("GIVE MONTH:"))
a = calendar.TextCalendar(calendar.SUNDAY)

calendar = a.formatmonth(year, month)

print (calendar)
