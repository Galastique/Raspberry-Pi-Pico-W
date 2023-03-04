import tm1637
from machine import Pin
from utime import sleep
mydisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

#show a time with colon
while True:
    mydisplay.brightness(7)
    mydisplay.numbers(12,54)
    sleep(0.25)
 
#adjust the brightness to make it loewr
#mydisplay.brightness(0)
#sleep(1)
 
#show scrolling text
#mydisplay.scroll("Hello World 123", delay=200)
#sleep(1)
 
#show temperature
#mydisplay.temperature(99)
#sleep(1)
 
#blank the screen again
#mydisplay.show(" ")