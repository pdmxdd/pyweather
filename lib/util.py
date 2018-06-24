import datetime

def printable_year(dt):
    return dt.year

def printable_month(dt):
    m = ""
    almost_m = dt.month
    if almost_m == 1:
        m = "January"
    elif almost_m == 2:
        m = "February"
    elif almost_m == 3:
        m = "March"
    elif almost_m == 4:
        m = "April"
    elif almost_m == 5:
        m = "May"
    elif almost_m == 6:
        m = "June"
    elif almost_m == 7:
        m = "July"
    elif almost_m == 8:
        m = "August"
    elif almost_m == 9:
        m = "September"
    elif almost_m == 10:
        m = "October"
    elif almost_m == 11:
        m = "November"
    elif almost_m == 12:
        m = "December"
    return m

def printable_day(dt):
    return dt.day

def printable_day_of_week(dt):
    day_of_w = ""
    almost_day_of_w = dt.weekday()
    if almost_day_of_w == 0:
        day_of_w = "Monday"
    elif almost_day_of_w == 1:
        day_of_w = "Tuesday"
    elif almost_day_of_w == 2:
        day_of_w = "Wednesday"
    elif almost_day_of_w == 3:
        day_of_w = "Thursday"
    elif almost_day_of_w == 4:
        day_of_w = "Friday"
    elif almost_day_of_w == 5:
        day_of_w = "Saturday"
    elif almost_day_of_w == 6:
        day_of_w = "Sunday"
    return day_of_w

def printable_hour(dt):
    almost_h = dt.hour
    h = almost_h % 12
    if h == 0:
        h = 12

    return h

def printable_meridian(dt):
    almost_h = dt.hour
    m = "PM"
    if almost_h < 12:
        m = "AM"

    return m

def printable_minute(dt):
    m = dt.minute
    if m < 10:
        m = "0" + str(m)

    return str(m)


def printable_time(current_time):
    readable_time = datetime.datetime.fromtimestamp(current_time)
    year = printable_year(readable_time)
    month = printable_month(readable_time)
    day = printable_day(readable_time)
    day_of_week = printable_day_of_week(readable_time)
    meridian = printable_meridian(readable_time)
    hour = printable_hour(readable_time)
    minute = printable_minute(readable_time)

    return year, month, day, day_of_week, hour, minute, meridian