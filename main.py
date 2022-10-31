from random import random
import time
import keyboard

print ("Press \"PrintScreen\" to begin printing code")
keyboard.wait('print screen')

usrCode = open("code.txt", "r")
for each in usrCode:
	for eachChar in each:
		keyboard.write(eachChar)
		time.sleep(random()/15)