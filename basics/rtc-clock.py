from ds1307 import DS1307
from utime import sleep

print(rtc.datetime())
year = int(input("Year : "))
month = int(input("month (Jan --> 1 , Dec --> 12): "))
date = int(input("date : "))
day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
hour = int(input("hour (24 Hour format): "))
minute = int(input("minute : "))
second = int(input("second : "))
now = (year,month,date,day,hour,minute,second,0)
rtc.datetime(now)
print(rtc.datetime())