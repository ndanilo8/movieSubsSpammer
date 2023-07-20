# Spammer with movie subtitles
# Author: Danilo Nascimento
# Contact: ndanilo8@hotmail.com

import pysrt
import time
import sys
import pyautogui as pg


def main(args):
    if len(args) < 4:
        print("Usage: python movieSpammer.py [file_name] [secs_to_wait] [secs_to_spam]")
        return

    file_name = args[1]
    secs_to_wait = int(args[2])
    secs_to_spam = int(args[3])

    try:
        subs = pysrt.open(file_name)
    except FileNotFoundError:
        print("File not found. Check the path to the file.")
        return

    print("Spamming movie subtitles...")
    for i in range(secs_to_wait, 0, -1):
        print(" ", i)
        time.sleep(1)

    print("Spamming begins!")
    for i, line in enumerate(subs):
        pg.write(line.text)
        pg.press('enter')

        # VERBOSE
        print("Subtitle no.", i+1, "out of", len(subs))
        time.sleep(secs_to_spam)


if __name__ == '__main__':
    main(sys.argv)
