from machine import I2C, Pin
from ds1307 import DS1307
from i2c_lcd import I2cLcd
import utime

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)

#Checks if RTC is detected
result = I2C.scan(i2c_rtc)
print(result)

#Shows RTC time
rtc = DS1307(i2c_rtc)
#print(rtc.datetime())

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