import machine, neopixel #Lib of devices with pins
import time

led = machine.Pin(25, machine.Pin.OUT)
neo_mood_pin = neopixel.NeoPixel(machine.Pin(4), 100)


def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


neo_mood_pin[0] = (255, 0, 0) # set to red, full brightness
neo_mood_pin[1] = (0, 128, 0) # set to green, half brightness
neo_mood_pin[2] = (0, 0, 64)  # set to blue, quarter brightness
neo_mood_pin.write()
time.sleep(3)

demo(neo_mood_pin)

while True:
    print('hello')
    led.value(1)
    time.sleep(0.2)
    led.value(0)
    time.sleep(0.2)

