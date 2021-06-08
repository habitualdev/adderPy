import lib.snip as snip
import lib.translate as translate
import os
n = 1
language = ['rus', 'chi_sim', 'chi_tra', 'kor', 'fra']
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
print("Begin selecting text.")
print("\r\n")

while True:
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
