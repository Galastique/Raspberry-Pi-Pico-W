from machine import Pin
from utime import sleep

led = Pin(13, Pin.OUT)

while True:
    led.toggle()
    sleep(0.5)