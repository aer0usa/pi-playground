from blinkt import set_pixel, set_brightness, show, clear
import time

sleepTime = 0.05
dim = 0.05
bright = 0.5

def doSweep():
    set_brightness(dim)
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

    clear()
    set_brightness(0)
    show()

def doFlash():
    for i in range(100):
        set_brightness(dim)
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

    clear()
    set_brightness(0)
    show()

