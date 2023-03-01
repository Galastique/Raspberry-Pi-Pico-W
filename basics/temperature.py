from machine import Pin
from utime import sleep
from dht import DHT22
 
sensor = DHT22(Pin(2)) 
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(f"Temperature: {temp}°C   Humidity: {hum:.0f}% ")
    sleep(2)