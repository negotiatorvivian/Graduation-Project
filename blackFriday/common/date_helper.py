# -*- coding:utf-8 -*-

import math
import time
import calendar
from datetime import datetime, timedelta, date


class Date(object):

    calendar_enums = [calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY, calendar.SATURDAY, calendar.SUNDAY]

    @classmethod
    def get_timestamp(cls, delta=0):
        timestamp = datetime.now() + timedelta(days=delta)
        return int(time.mktime(timestamp.timetuple()))

    @classmethod
    def get_date_timestamp(cls, datetime, day = 0, hour = 0):
        timestamp = datetime + timedelta(days = day, hours = hour)
        return int(time.mktime(timestamp.timetuple()))
    
    @classmethod
    def get_day_stamp(cls, delta=0):
        day = date.today() + timedelta(days=delta)
        return int(time.mktime(day.timetuple()))

    @classmethod
    def get_zero_stamp_from_timestamp(cls, timestamp):
        ltime=time.localtime(timestamp)
        timeStr=time.strftime("%Y-%m-%d", ltime)
        date_time = timeStr.split('-')
        return time.mktime(datetime(int(date_time[0]), int(date_time[1]), int(date_time[2])).timetuple())

    @classmethod
    def get_month_stamp(cls):
        day = date.today()
        day_month = date(day.year, day.month, 1)
        return int(time.mktime(day_month.timetuple()))

    @classmethod
    def round_day_stamp(cls, timestamp):
        day = date.fromtimestamp(timestamp)
        return int(time.mktime(day.timetuple()))
    
    @classmethod
    def get_day_begin(cls, ts=time.time(), N=0):
         return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime(ts)), '%Y-%m-%d'))) - 86400 * N

    @classmethod
    def round_week_stamp(cls, timestamp):
        day = date.fromtimestamp(timestamp)
        day_week = day - timedelta(days=day.weekday())
        return int(time.mktime(day_week.timetuple()))
    
    @classmethod
    def get_date_span(cls, timestamp1, timestamp2):
        day1 = date.fromtimestamp(timestamp1)
        day2 = date.fromtimestamp(timestamp2)
        return int(math.fabs((day1 - day2).days))


    @classmethod
    def round_month_stamp(cls, timestamp):
        day = date.fromtimestamp(timestamp)
        day_month = date(day.year, day.month, 1)
        return int(time.mktime(day_month.timetuple()))


    @classmethod
    def round_month_laststamp(cls, timestamp):
        day = date.fromtimestamp(timestamp)
        day_month = date(day.year, day.month + 1, 1) + timedelta(days=-1)
        return int(time.mktime(day_month.timetuple()))


    @classmethod
    def round_year_stamp(cls, timestamp):
        day = date.fromtimestamp(timestamp)
        day_year = date(day.year, 1, 1)
        return int(time.mktime(day_year.timetuple()))

    @classmethod
    def last_week_stamp(cls):
        today = date.today()
        weekday = today.weekday()
        start_delta = timedelta(days=weekday, weeks=1)
        start_of_week = today - start_delta
        return int(time.mktime(start_of_week.timetuple()))

    @classmethod
    def next_week_stamp(cls):
        today = date.today()
        weekday = today.weekday()
        start_delta = timedelta(days=weekday, weeks=-1)
        start_of_week = today - start_delta
        return int(time.mktime(start_of_week.timetuple()))

    '''
    时间字符串转秒
    字符串格式: %Y-%m-%d %H:%M:%S
    '''
    @classmethod
    def timestamp_from_datestr(cls, datestr):
        date, ht = datestr.split(' ')
        date = date.split('-')
        ht = ht.split(':')
        return time.mktime(datetime(int(date[0]), int(date[1]), int(date[2]), int(ht[0]), int(ht[1]), int(ht[2])).timetuple())

    @classmethod
    def timestamp_from_daystr(cls, datestr):
        date = datestr.split('-')
        return time.mktime(datetime(int(date[0]), int(date[1]), int(date[2])).timetuple())


    @classmethod
    def last_month_stamp(cls):
        today = date.today()
        this_month_start = datetime(today.year, today.month, 1)
        last_month_end = this_month_start - timedelta(days=1)
        last_month_start = datetime(last_month_end.year, last_month_end.month, 1)
        ts = int(time.mktime(last_month_start.timetuple()))
        return ts, last_month_end.day

    @classmethod
    def next_month_stamp(cls):
        today = date.today()
        month = (today.month + 1) % 12
        year = today.year + (today.month + 1) / 12
        next_month_start = datetime(year, month, 1)
        ts = int(time.mktime(next_month_start.timetuple()))
        return ts

    @classmethod
    def get_date_from_stamp(cls, timestamp):
        date_tuple = date.fromtimestamp(timestamp)
        return str(date_tuple)

    @classmethod
    def birthday_to_age(cls, year):
        return date.today().year - int(year)

    @classmethod
    def date_from_timestamp(cls, timestamp):
        return date.fromtimestamp(timestamp)

    @classmethod
    def timestamp_to_datetime(cls, timestamp, format = '%Y-%m-%d %H:%M:%S'):
        return time.strftime(format, time.localtime(timestamp))

    @classmethod
    def timestamp_to_date(cls, timestamp, format = '%Y-%m-%d'):
        return time.strftime(format, time.localtime(timestamp))

    @classmethod
    def datetime_from_timestamp(cls, timestamp):
        return datetime.fromtimestamp(timestamp)

    @classmethod
    def get_next_weekday(cls, date, target_weekday, next_week = 0):
        oneday = timedelta(days = 1)
        if next_week == 1:
            if date.weekday() == cls.calendar_enums[target_weekday]:
                date += oneday
        while date.weekday() != cls.calendar_enums[target_weekday]:
            date += oneday
        return datetime.combine(date,datetime.min.time())

    @classmethod
    def get_last_weekday(cls, date, target_weekday):
        oneday = timedelta(days = 1)
        while date.weekday() != cls.calendar_enums[target_weekday]:
            date -= oneday
        return datetime.combine(date,datetime.min.time())

    @classmethod
    def age_to_timestamp(cls, age):
        year = int(time.strftime('%Y', time.localtime()))
        year = year - int(age)
        year = date(year, 1, 1)
        return int(time.mktime(year.timetuple()))

    @classmethod
    def age_to_year(cls, age):
        year = int(time.strftime('%Y', time.localtime()))
        return year - int(age)

    @classmethod
    def timestamp_from_date(cls, date):
        date = date.split('-')
        return time.mktime(datetime(int(date[0]), int(date[1]), int(date[2])).timetuple())

    @classmethod
    def date_from_datetime(cls, datetime):
        return time.strftime('%F %H:%M:%S', datetime.timetuple())
        
    @classmethod
    def get_datetime(cls, delta = 0):
        datetime_of_days = datetime.now() + timedelta(days = delta)
        datetime_of_days_format = datetime_of_days.strftime('%Y-%m-%d %H:%M:%S')
        return datetime_of_days_format

    @classmethod
    def get_date_time(cls, dateStr = '', delta = 0):
        if dateStr == '':
            dateStr = date.today()
        else:
            dateStr = datetime.strptime(dateStr, '%Y-%m-%d').date()
        date_of_days = dateStr + timedelta(days = delta)
        date_of_days_format = date_of_days.strftime('%Y-%m-%d')
        return date_of_days_format


    @classmethod
    def get_date(cls, delta = 0):
        date_of_days = date.today() + timedelta(days = delta)
        date_of_days_format = date_of_days.strftime('%Y-%m-%d')
        return date_of_days_format
