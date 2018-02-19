from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.1)

sleepTime = 0.01

while True:
    for i in range(256):
        clear()
        set_pixel(0, i, (i + 85) % 255, (i + 170) % 255)
        # set_pixel(0, 0, (i + 85) % 255, 0)
        show()
        time.sleep(sleepTime)

    for i in range(256):
        j = 255 - i
        clear()
        set_pixel(0, j, (j + 85) % 255, (j + 170) % 255)
        # set_pixel(0, 0, (j + 85) % 255, 0)
        show()
        time.sleep(sleepTime)
