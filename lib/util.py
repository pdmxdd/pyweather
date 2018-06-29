import datetime
import googlemaps
from enviropy.util import get_enviropy
import requests


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


def printable_time_string(current_time):
    year, month, day, day_of_week, hour, minute, meridian = printable_time(current_time)
    return "{} {} {} {} {}:{} {}".format(day_of_week, month, day, year, hour, minute, meridian)


def printable_sun(sunrise_time):
    readable_time = datetime.datetime.fromtimestamp(sunrise_time)
    meridian = printable_meridian(readable_time)
    hour = printable_hour(readable_time)
    minute = printable_minute(readable_time)
    return "{}:{} {}".format(hour, minute, meridian)


def get_location_data_from_address(address_string):
    enviropy = get_enviropy()
    gmaps = googlemaps.Client(key=enviropy["GOOGLE_API"])
    geocode_result = gmaps.geocode(address_string)
    lat = geocode_result[0]['geometry']['location']['lat']
    long = geocode_result[0]['geometry']['location']['lng']
    formatted_address = geocode_result[0]['formatted_address']
    place_id = geocode_result[0]['place_id']
    return lat, long, formatted_address, place_id


def get_lat_long_from_address(address_string):
    enviropy = get_enviropy()
    gmaps = googlemaps.Client(key=enviropy["GOOGLE_API"])
    geocode_result = gmaps.geocode(address_string)
    lat = geocode_result[0]['geometry']['location']['lat']
    long = geocode_result[0]['geometry']['location']['lng']
    return lat, long


def get_weather_from_address(address_string):
    enviropy = get_enviropy()
    lat, long = get_lat_long_from_address(address_string)
    r = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(enviropy["API_KEY"], lat, long))
    data = r.json()
    current_summary = data["currently"]["summary"]
    current_temp_f = data["currently"]["temperature"]
    current_time = data["currently"]["time"]
    current_humidity = data["currently"]["humidity"]
    current_uv = data["currently"]["uvIndex"]
    time_string = printable_time_string(current_time)
    print(time_string)
    print("Currently in Crestwood")
    print("{}".format(current_summary))
    print("{}F".format(current_temp_f))
    print("{}% Humidity".format(current_humidity * 100))
    print("UV Index: {}".format(current_uv))
    print("Sunrise: {}".format(printable_sun(data["daily"]["data"][0]["sunriseTime"])))
    print("Sunset: {}".format(printable_sun(data["daily"]["data"][0]["sunsetTime"])))
