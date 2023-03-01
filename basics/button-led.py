from machine import Pin
from utime import sleep_ms

button = Pin(16, Pin.IN, Pin.PULL_UP)
led = Pin(13, Pin.OUT)

try:
    while True:
        if button.value():
            print("no button?")
            led.off()
        else:
            print("button :)")
            led.on()
        sleep_ms(50)
except:
    pass
