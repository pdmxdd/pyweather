import requests
import os

API_KEY = os.environ["DARKSKY_API"]
C_LAT = "38.557552"
C_LONG = "-90.376152"

if __name__ == "__main__":
    print("heyo")
    r = requests.get("https://api.darksky.net/forecast/{}/{},{}".format(API_KEY, C_LAT, C_LONG))
    data = r.json()
    # print(data)
    print(data["currently"]["summary"])
    print(data["currently"]["temperature"])
    print(data["daily"]["data"][0]["sunriseTime"])
    print(data["daily"]["data"][0]["sunsetTime"])