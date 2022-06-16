import os
import keyboard
from pynput.mouse import Listener

steps = input("How Many Steps?")
step = int(steps)
os.system('sudo rm generatedcode.py && sudo rm poz.txt')
with open("generatedcode.py", "a") as text_file:
                text_file.write('import pyautogui \n')
with open("generatedcode.py", "a") as text_file:
                text_file.write('import time \n')
with open("generatedcode.py", "a") as text_file:
                text_file.write('time.sleep(10) \n')
def is_clicked(x, y, button, pressed):
    if pressed:
        os.system('eval $(xdotool getmouselocation --shell) && echo $X "," $Y > poz.txt')
        with open('poz.txt', 'r') as file:
            data = file.read().rstrip()
            stripped = 'pyautogui.click(' + data.replace(' , ', ', ') + ')' + '\n' + 'time.sleep(3)\n'
            with open("generatedcode.py", "a") as text_file:
                text_file.write(stripped)
        return False # to stop the thread after click
for x in range(0, step):
    with Listener(on_click=is_clicked) as listener:
        listener.join()
os.system('sudo rm poz.txt')

