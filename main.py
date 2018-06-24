import requests
import os
from lib.util import printable_time

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