from machine import Pin
from utime import sleep

led = Pin("LED")

while True:
    led.toggle()
    sleep(0.5)
