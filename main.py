# import requests
# import googlemaps
# import os
# from lib.util import printable_time
# from lib.util import printable_time_string, printable_sun

# from enviropy.util import get_enviropy
from lib.util import get_weather_from_address

# enviropy = get_enviropy()

# API_KEY = enviropy["API_KEY"]
# _LAT = enviropy["C_LAT"]
# C_LONG = enviropy["C_LONG"]

if __name__ == "__main__":
    '''
    r = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(API_KEY, C_LAT, C_LONG))
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
    print("UV Index: {}".format(current_uv))
    print("Sunrise: {}".format(printable_sun(data["daily"]["data"][0]["sunriseTime"])))
    print("Sunset: {}".format(printable_sun(data["daily"]["data"][0]["sunsetTime"])))
    '''
    addr = "511 Joshua Drive, Crestwood, MO"
    get_weather_from_address(addr)