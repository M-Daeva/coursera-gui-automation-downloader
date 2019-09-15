import pyperclip
import pyautogui as pag
import keyboard as kb
import time


def get_downloaders(coords):
    def download(cnt=1):
        pag.hotkey('home')
        time.sleep(1)
        pag.moveTo(*coords.play, 0.5)
        pag.click()

        pag.moveTo(*coords.quality360, 0.5)
        pag.moveTo(*coords.quality720, 0.5)
        pag.click()

        pag.moveTo(*coords.title, 0.5)
        pag.click()
        pag.drag(coords.title_length, duration=1)
        pag.hotkey('ctrl', 'c')
        data = pyperclip.paste().strip().replace('?', '').replace(':', ' -').replace('"', "'") \
            .replace('/', ', ')
        pag.click()

        pag.moveTo(*coords.play, 0.5)
        time.sleep(3)
        pag.click(button='right')
        pag.moveTo(*coords.save_option, 0.5)
        pag.click()
        time.sleep(4)
        kb.write(f'{cnt} {data}.webm')
        pag.hotkey('enter')
        time.sleep(1)
        pag.moveTo(*coords.end_of_video, 0.5)
        pag.click()
        time.sleep(5)
        pag.moveTo(*coords.next_video, duration=0.5)
        pag.click()
        time.sleep(6)

    def download_all(start=1):
        cnt = start

        while True:
            download(cnt)
            cnt += 1

    class Downloaders:
        def __init__(self):
            self.download = download
            self.download_all = download_all

    return Downloaders()
