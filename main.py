import requests
import os
import datetime

API_KEY = os.environ["DARKSKY_API"]
C_LAT = "38.557552"
C_LONG = "-90.376152"

if __name__ == "__main__":
    r = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(API_KEY, C_LAT, C_LONG))
    data = r.json()
    # print(data)
    current_summary = data["currently"]["summary"]
    current_temp_f = data["currently"]["temperature"]
    current_time = data["currently"]["time"]
    #readable_time = time.localtime(current_time)
    readable_time = datetime.datetime.fromtimestamp(current_time)
    year = readable_time.year
    month = readable_time.month
    day = readable_time.day
    almost_day_of_week = readable_time.weekday()
    day_of_week = ""
    if int(almost_day_of_week) == 0:
        day_of_week = "Monday"
    elif int(almost_day_of_week) == 1:
        day_of_week = "Tuesday"
    elif int(almost_day_of_week) == 2:
        day_of_week = "Wednesday"
    elif int(almost_day_of_week) == 3:
        day_of_week = "Thursday"
    elif int(almost_day_of_week) == 4:
        day_of_week = "Friday"
    elif int(almost_day_of_week) == 5:
        day_of_week = "Saturday"
    elif int(almost_day_of_week) == 6:
        day_of_week = "Sunday"

    almost_hour = readable_time.hour
    minute = readable_time.minute
    print("{} {} {} {}".format(day_of_week, month, day, year))
    print(readable_time)
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