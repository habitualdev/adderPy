import os
import lib.snip as snip
import lib.translate as translate
from pynput import keyboard


def pull_and_process():
    try:
        area = snip.GetArea()
        image = area.snip()
        translated_string = translate.translate(image, language[choice])
        print(translated_string)
    except SystemError:
        print("Bad box selection. Requires selecting with top left corner, then bottom right corner.\r\n")
    except KeyboardInterrupt:
        print("Goodbye")
        exit()


class RunApp:
    def __init__(self):
        with keyboard.GlobalHotKeys({'<ctrl>+<alt>+t': self.on_activate_t}) as self.l:
            self.l.join()

    def on_activate_t(self):
        print("Now select your text.")
        pull_and_process()




n = 1
language = ['rus', 'chi_sim', 'chi_tra', 'kor', 'fra', 'Arabic']
loop = True

print("Easy OCR + Translate through a terminal - Without Cut and Paste!")
print("Choose your language")



for lan in language:
    print(str(n) + ": " + str(lan))
    n = n + 1

while loop:
    try:
        choice = int(input()) - 1
        loop = False
    except ValueError:
        print("Bad selection, try again.")
        loop = True

os.system("clear")
print("You chose " + language[choice])
print("Press \"Ctrl+Alt+T\" to begin.")


while True:
    try:
        app = RunApp()
    except KeyboardInterrupt:
        exit()