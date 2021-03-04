import time
import rotatescreen
screen = rotatescreen.get_primary_display()
while True:
    time.sleep(0.1)
    screen.rotate_to(90)