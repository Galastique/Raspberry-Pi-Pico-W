from machine import I2C, Pin
from utime import sleep
from i2c_lcd import I2cLcd

#LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
LCD = I2cLcd(i2c, I2C_ADDR, 2, 16)

#Writes text
lcd.putstr("Help, Im trapped\nin the computer!")