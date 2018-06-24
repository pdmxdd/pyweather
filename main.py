import requests
import os
import datetime

API_KEY = os.environ["DARKSKY_API"]
C_LAT = "38.557552"
C_LONG = "-90.376152"

def printable_year(dt):
    out_year = dt.year
    return out_year

def printable_month(dt):
    month = ""
    almost_month = dt.month
    if almost_month == 1:
        month = "January"
    elif almost_month == 2:
        month = "February"
    elif almost_month == 3:
        month = "March"
    elif almost_month == 4:
        month = "April"
    elif almost_month == 5:
        month = "May"
    elif almost_month == 6:
        month = "June"
    elif almost_month == 7:
        month = "July"
    elif almost_month == 8:
        month = "August"
    elif almost_month == 9:
        month = "September"
    elif almost_month == 10:
        month = "October"
    elif almost_month == 11:
        month = "November"
    elif almost_month == 12:
        month = "December"
    return month

def printable_day(dt):
    return dt.day

def printable_day_of_week(dt):
    day_of_week = ""
    almost_day_of_week = dt.weekday()
    if almost_day_of_week == 0:
        day_of_week = "Monday"
    elif almost_day_of_week == 1:
        day_of_week = "Tuesday"
    elif almost_day_of_week == 2:
        day_of_week = "Wednesday"
    elif almost_day_of_week == 3:
        day_of_week = "Thursday"
    elif almost_day_of_week == 4:
        day_of_week = "Friday"
    elif almost_day_of_week == 5:
        day_of_week = "Saturday"
    elif almost_day_of_week == 6:
        day_of_week = "Sunday"
    return day_of_week

def printable_hour(dt):
    almost_hour = dt.hour
    hour = almost_hour % 12
    if hour == 0:
        hour = 12

    return hour

def printable_meridian(dt):
    almost_hour = dt.hour
    meridian = "PM"
    if almost_hour < 12:
        meridian = "AM"

    return meridian

def printable_minute(dt):
    minute = dt.minute
    if minute < 10:
        minute = "0" + str(minute)

    return minute


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


if __name__ == "__main__":
    r = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(API_KEY, C_LAT, C_LONG))
    data = r.json()
    # print(data)
    current_summary = data["currently"]["summary"]
    current_temp_f = data["currently"]["temperature"]
    current_time = data["currently"]["time"]
    #readable_time = time.localtime(current_time)
    year, month, day, day_of_week, hour, minute, meridian = printable_time(current_time)

    print("{} {} {} {} {}:{} {}".format(day_of_week, month, day, year, hour, minute, meridian))
    #print(readable_time)
    current_humidity = data["currently"]["humidity"]
    current_uv = data["currently"]["uvIndex"]
    print("Currently in Crestwood")
    print("It is currently {}".format(current_time))
    print("{}".format(current_summary))
    print("{}F".format(current_temp_f))
    print("UV Index: {}".format(current_uv))
    #print(data["currently"]["summary"])
    #print(data["currently"]["temperature"])
    #print(data["daily"]["data"][0]["sunriseTime"])
    #print(data["daily"]["data"][0]["sunsetTime"])
    #print(data["daily"]["data"][0]["summary"])