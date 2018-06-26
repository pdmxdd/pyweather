import requests
import os
# from lib.util import printable_time
from lib.util import printable_time_string, printable_sun

from enviropy.util import get_enviropy

enviropy = get_enviropy()

API_KEY = enviropy["API_KEY"]
C_LAT = enviropy["C_LAT"]
C_LONG = enviropy["C_LONG"]

if __name__ == "__main__":
    r = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(API_KEY, C_LAT, C_LONG))
    data = r.json()
    # print(data)
    current_summary = data["currently"]["summary"]
    current_temp_f = data["currently"]["temperature"]
    current_time = data["currently"]["time"]
    current_humidity = data["currently"]["humidity"]
    current_uv = data["currently"]["uvIndex"]
    #readable_time = time.localtime(current_time)
    # year, month, day, day_of_week, hour, minute, meridian = printable_time(current_time)

    # print("{} {} {} {} {}:{} {}".format(day_of_week, month, day, year, hour, minute, meridian))
    time_string = printable_time_string(current_time)
    print(time_string)
    #print(readable_time)
    print("Currently in Crestwood")
    # print("It is currently {}".format(current_time))
    print("{}".format(current_summary))
    print("{}F".format(current_temp_f))
    print("UV Index: {}".format(current_uv))
    print("Sunrise: {}".format(printable_sun(data["daily"]["data"][0]["sunriseTime"])))
    print("Sunset: {}".format(printable_sun(data["daily"]["data"][0]["sunsetTime"])))
    #print(data["currently"]["summary"])
    #print(data["currently"]["temperature"])
    #print(data["daily"]["data"][0]["sunriseTime"])
    #print(data["daily"]["data"][0]["sunsetTime"])
    #print(data["daily"]["data"][0]["summary"])