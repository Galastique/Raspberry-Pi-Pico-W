from machine import Pin, PWM
from utime import sleep_ms

#Buzzer
buzzer = PWM(Pin(15))

def setLoudness(loudness):
    buzzer.duty_u16(loudness)

def setFrequency(frequency):
    buzzer.freq(frequency)

#Plays full range of sound
setLoudness(1000)
for x in range(10, 12000):
    buzzer.freq(x)
    sleep_ms(2)

#Stops sound
buzzer.duty_u16(0)