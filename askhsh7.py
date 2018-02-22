import datetime

wday = datetime.date.today().strftime("%A")

day = datetime.date.today().day

month = datetime.date.today().month

year = datetime.date.today().year

counter = 0

for i in range(10):

    while month <=12:

        e = datetime.date(year,month,day)

        if e.strftime("%A") == wday:

           counter = counter + 1

        month = month + 1

    year = year + 1

    month = 1

print "There are ",counter,"days including today"

