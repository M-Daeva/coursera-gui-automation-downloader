import pyautogui as pag
import time


def get_coords():
    while True:
        time.sleep(1)
        x, y, = pag.position()
        print(x, y)
        if x < 50 and y < 50:
            break
