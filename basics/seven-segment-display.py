from tm1637 import TM1637
from machine import Pin
from utime import sleep

display = TM1637(clk=Pin(1), dio=Pin(0))
display.brightness(7)

#Display 1 number
#display.number(21)

#Display 2 numbers
while True:
    display.brightness(7)
    display.numbers(12,54)
    sleep(0.25)
 
#Display text
#mydisplay.show("Pico")

#Display scrolling text
#display.scroll("balls", delay=200)
 
#Display temperature
#display.temperature(69)
 
#Clear screen
#display.show(" ")