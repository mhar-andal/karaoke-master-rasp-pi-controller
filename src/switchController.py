#!/usr/bin/python

# External Modules
import RPi.GPIO as GPIO
import time

# pin 2 corresponds to button press 1 
BUTTON1 = 2
BUTTON2 = 3
BUTTON3 = 4
BUTTON4 = 14
BUTTON5 = 15
BUTTON6 = 18
BUTTON7 = 17
BUTTON8 = 27
BUTTON9 = 22
BUTTON10 = 23
#RSV 
BUTTON11 = 10

class buttonPress:
	def __init__(self, pin, state):
		self.pin = pin
		self.state = state

def config(trigger):

	# follows pin numbers listed on header P1
	GPIO.setmode(GPIO.BCM)

	# could optionally be GPIO.LOW / 0 / false
	# out_List = {11,12}
	GPIO.setup(trigger.pin, GPIO.OUT)
	print("Writing %d to pin %d" % (trigger.state, trigger.pin))
	GPIO.output(trigger.pin, trigger.state)

	# WE CANNOT DO THIS SINCE WE CANNOT TRIGGER MULTIPLE AT THE SAME TIME 
	# GPIO.output(out_List, GPIO.LOW)

	# INSTEAD WE MUST WRITE A FUNCTION THAT TAKES AS INPUT THE PIN TO SET LOW
	# WE THEN SET THE PIN LOW AND CALL A FUNCTION TO WAIT AND REPEAT

def changeButton(trigger, pin, state):

	trigger.pin = pin
	trigger.state = state

	config(trigger)

def changeState(trigger):

	if trigger.state == GPIO.LOW:
		trigger.state = GPIO.HIGH
	else:
		trigger.state = GPIO.LOW

	GPIO.output(trigger.pin, trigger.state)

def wait():
	print("Waiting 200 ms")
	time.sleep(.2)

def clean():
	print("Cleaning GPIO")
	GPIO.cleanup()

def runInput(arr):
	arr.append(11)
	trigger = buttonPress(0, GPIO.LOW)
	config(trigger)
	wait()
	for num in arr:
		changeButton(trigger, eval('BUTTON' + str(num)), GPIO.LOW)
		wait()
		changeState(trigger)
		wait()
		changeState(trigger)
		clean()

#def main():
	#print("Program Running...")

	# pass the 'BCM' equivalent pin number and 0/1 for LOW/HIGH
	#arr = [1,3,6,6,4]


	#arr.append(11)

	#runInput(arr)


#main()











