from machine import Pin
from utime import sleep

button = Pin(16, Pin.IN, Pin.PULL_UP)

try:
    while True:
        if button.value():
            print("no button?")
        else:
            print("button :)")
        sleep(0.5)
except:
    pass