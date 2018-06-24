import unittest
import datetime

from lib.util import printable_year,\
    printable_month, printable_day,\
    printable_day_of_week,\
    printable_hour,\
    printable_meridian,\
    printable_minute,\
    printable_time,\
    printable_time_string

class YearTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 0, 4, 10)
        self.d2 = datetime.datetime(2014, 7, 25)
        self.d3 = datetime.datetime(1776, 7, 4)

    def test_year(self):
        self.assertEqual(2018, printable_year(self.d1))
        self.assertEqual(2014, printable_year(self.d2))
        self.assertEqual(1776, printable_year(self.d3))

class MonthTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 0, 4, 10)
        self.d2 = datetime.datetime(2014, 1, 25)
        self.d3 = datetime.datetime(1776, 12, 4)

    def test_month(self):
        self.assertEqual("June", printable_month(self.d1))
        self.assertEqual("January", printable_month(self.d2))
        self.assertEqual("December", printable_month(self.d3))

class DayTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 0, 4, 10)
        self.d2 = datetime.datetime(2014, 1, 1)
        self.d3 = datetime.datetime(1776, 12, 31)

    def test_day(self):
        self.assertEqual(24, printable_day(self.d1))
        self.assertEqual(1, printable_day(self.d2))
        self.assertEqual(31, printable_day(self.d3))

class DayOfWeekTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24)
        self.d2 = datetime.datetime(1989, 6, 1)
        self.d3 = datetime.datetime(2024, 12, 25)

    def test_day_of_week(self):
        self.assertEqual("Sunday", printable_day_of_week(self.d1))
        self.assertEqual("Thursday", printable_day_of_week(self.d2))
        self.assertEqual("Wednesday", printable_day_of_week(self.d3))

class HourTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 12, 0, 0)
        self.d2 = datetime.datetime(2018, 6, 24, 0, 0, 0)
        self.d3 = datetime.datetime(2018, 6, 24, 3, 0, 0)
        self.d4 = datetime.datetime(2018, 6, 24, 18, 0, 0)

    def test_hour(self):
        self.assertEqual(12, printable_hour(self.d1))
        self.assertEqual(12, printable_hour(self.d2))
        self.assertEqual(3, printable_hour(self.d3))
        self.assertEqual(6, printable_hour(self.d4))

class MeridianTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 12, 0, 0)
        self.d2 = datetime.datetime(2018, 6, 24, 0, 0, 0)
        self.d3 = datetime.datetime(2018, 6, 24, 3, 0, 0)
        self.d4 = datetime.datetime(2018, 6, 24, 18, 0, 0)

    def test_meridian(self):
        self.assertEqual("PM", printable_meridian(self.d1))
        self.assertEqual("AM", printable_meridian(self.d2))
        self.assertEqual("AM", printable_meridian(self.d3))
        self.assertEqual("PM", printable_meridian(self.d4))

class MinuteTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 12, 0, 0)
        self.d2 = datetime.datetime(2018, 6, 24, 0, 15, 0)
        self.d3 = datetime.datetime(2018, 6, 24, 3, 59, 0)
        self.d4 = datetime.datetime(2018, 6, 24, 18, 8, 0)

    def test_minute(self):
        self.assertEqual("00", printable_minute(self.d1))
        self.assertEqual("15", printable_minute(self.d2))
        self.assertEqual("59", printable_minute(self.d3))
        self.assertEqual("08", printable_minute(self.d4))

class TimeTest(unittest.TestCase):
    def setUp(self):
        d1 = datetime.datetime(2018, 6, 24, 12, 0, 0)
        self.year = printable_year(d1)
        self.month = printable_month(d1)
        self.day = printable_day(d1)
        self.day_of_week = printable_day_of_week(d1)
        self.hour = printable_hour(d1)
        self.meridian = printable_meridian(d1)
        self.minute = printable_minute(d1)

    def test_year(self):
        self.assertEqual(2018, self.year)

    def test_month(self):
        self.assertEqual("June", self.month)

    def test_day(self):
        self.assertEqual(24, self.day)

    def test_day_of_week(self):
        self.assertEqual("Sunday", self.day_of_week)

    def test_hour(self):
        self.assertEqual(12, self.hour)

    def test_meridian(self):
        self.assertEqual("PM", self.meridian)

    def test_minute(self):
        self.assertEqual("00", self.minute)

class PrintableTimeTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 12, 0, 0)

    def test_printable_time(self):
        self.assertEqual((2018, "June", 24, "Sunday", 12, "00", "PM"), printable_time(self.d1.timestamp()))

class PrintableStringTimeTest(unittest.TestCase):
    def setUp(self):
        self.d1 = datetime.datetime(2018, 6, 24, 12, 0, 0)

    def test_string_time(self):
        self.assertEqual("Sunday June 24 2018 12:00 PM", printable_time_string(self.d1.timestamp()))