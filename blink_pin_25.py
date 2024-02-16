import machine #Lib of devices with pins
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    print('hello')
    led.value(1)
    utime.sleep(0.2)
    led.value(0)
    utime.sleep(0.2)
