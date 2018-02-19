from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.1)

sleepTime = 0.01
dim = 0.05
bright = 0.5

while True:
    for i in range(100):
        set_brightness(0.1)
        clear()
        if (i == 0):
            set_pixel(0, 255, 255, 255, dim)
            set_pixel(7, 255, 255, 255, dim)
        elif (i == 25):
            set_pixel(1, 0, 0, 255, bright)
            set_pixel(6, 0, 0, 255, bright)
        elif (i == 50):
            set_pixel(3, 255, 0, 0, dim)
            set_pixel(4, 255, 0, 0, dim)
        elif (i == 75):
            set_pixel(2, 255, 255, 0, dim)
            set_pixel(5, 255, 255, 0, dim)
        show()
        time.sleep(sleepTime)

