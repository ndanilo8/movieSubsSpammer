from ast import arg
import pyautogui as pg
import time
import random
import sys
import requests

# you need to have python installed on your system
# and some extra libraries
# $ pip install pyautogui
# $ pip install requests


# TO RUN SPAMMER:
# $ python spammer.py [mode: 1 or 2] [amount of msgs to spam] [interval between msgs in secs]
# EXAMPLE
# $ python spammer.py 1 100 .5


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
website_words = requests.get(word_site).text.splitlines()


print("\n\n SPAM BOT \n\n")

# add your terms...
message = "Testing this spammer"


def startTimer():
	counter = 6
	for i in range(6):
		counter -= 1
		print(" Starting in...", counter, "secs")
		time.sleep(1)


def randomSpam(words):
	#message = words.split()
	message = random.choice(words)
	pg.write(message)
	pg.press('enter')


def messageSpam(msg):
	pg.write(msg)
	pg.press('enter')


def main(args):
	mode = int(args[1])
	amount = int(args[2])
	interval = float(args[3])
	
	startTimer()
	for i in range(amount):
		print(" msg no.", i, "out of", amount)
        
		if mode == 1: # Random Mode
			randomSpam(website_words)

		if mode == 2: # Send specific message
			messageSpam(message)
		time.sleep(interval)



if __name__ == '__main__':
    main(sys.argv)
