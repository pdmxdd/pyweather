import time
from lib.util import get_weather_from_address

def clear_screen():
    print("\n" * 40)

def print_separator():
    print("-" * 40)

if __name__ == "__main__":
    #for i in range(3):
        clear_screen()
        print_separator()
        addr = "511 Joshua Drive, Crestwood, MO"
        get_weather_from_address(addr)
        print_separator()
        #time.sleep(120)
