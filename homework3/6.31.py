import time
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthname = ["Janurary", "February", "March", "April", "May",
             "June", "July", "August", "September", "October", "November", "December"]
currentTime = time.time()

totalSeconds = int(currentTime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds//60

currentMinute = totalMinutes % 60

totalHours = totalMinutes//60

currentHour = totalHours % 24

totalDays = totalHours//24


def isleapYear(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def getYearMonthDay(days):
    year = 1969
    while days > 0:
        year += 1
        if isleapYear(year):
            days -= 366
        else:
            days -= 365
    if isleapYear(year):
        days += 366
    else:
        days += 365
    month = 0
    while days > 0:
        month += 1
        if month == 2:
            if isleapYear(year):
                days -= 29
            else:
                days -= 28
        else:
            days -= months[month-1]
    if month == 2:
        if isleapYear(year):
            days += 29
        else:
            days += 28
    else:
        days += months[month-1]
    days+=1
    return year, month, days


year, month, day = getYearMonthDay(totalDays)
print("Current date and time is", monthname[month-1], day,",",year,currentHour,
      ":", currentMinute, ":", currentSecond)
