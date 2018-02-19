from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.05)

sleepTime = 0.1

while True:
    for i in range(8):
        clear()
        j = i + 1
        k = 8 - i
        set_pixel(i, (255 // j), (255 // k), 0)
        show()
        time.sleep(sleepTime)

    for i in range(8):
        clear()
        j = i + 1
        k = 8 - i
        set_pixel(k-1, (255 // k), (255 // j), 0)
        show()
        time.sleep(sleepTime)
