import calendar

def displayallmonths(year):
    for month in range(1, 13):
        print(calendar.month(year, month))
        print("-" * 30)

year = int(input("Enter the year: "))
displayallmonths(year)