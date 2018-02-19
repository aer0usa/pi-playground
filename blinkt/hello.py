from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.05)

clear()
set_pixel(0, 255, 255, 255)
show()

time.sleep(1.0)
clear()
show()

time.sleep(0.25)
clear()
set_pixel(0, 255, 0, 0)
set_pixel(1, 255, 255, 0)
set_pixel(2, 0, 255, 0)
show()

time.sleep(1.0)
clear()
show()

time.sleep(0.25)
clear()
set_pixel(0, 255, 0, 0)
set_pixel(1, 255, 255, 0)
set_pixel(2, 0, 255, 0)
show()

time.sleep(1.0)
clear()
show()
