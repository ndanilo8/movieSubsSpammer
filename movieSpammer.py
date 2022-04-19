# Spammer with movie subtitles
# Author: Danilo Nascimento
# Contact: ndanilo8@hotmail.com


# run as: python movieSpammer.py [secs to wait] [interval between messages in secs]

import pysrt
import time
import sys
import pyautogui as pg


def main(args):
    file_name = args[1]
    secs_to_wait = args[2]
    secs_to_spam = args[3]
    try:
        subs = pysrt.open(file_name)
    except:
       print("check path to file!")

    print("Spam some fu**ing movie subtitles")
    for i in range(int(secs_to_wait)):
        i += 1  # start counting from 1 instead of 0
        print(" ", i)
        time.sleep(1)

    for i in range(len(subs)):
        line = subs[i]
        pg.write(line.text)
        pg.press('enter')

        # VERBOSE
        print("subtitle no.", i, "out of", len(subs))
        time.sleep(int(secs_to_spam))


if __name__ == '__main__':
    main(sys.argv)
