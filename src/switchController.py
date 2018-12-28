#!/usr/bin/python

# External Modules
import RPi.GPIO as GPIO
import time

def config():

	# follows pin numbers listed on header P1
	GPIO.setmode(GPIO.BCM)

	# could optionally be GPIO.LOW / 0 / false
	# out_List = {11,12}
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.LOW)

	# WE CANNOT DO THIS SINCE WE CANNOT TRIGGER MULTIPLE AT THE SAME TIME 
	# GPIO.output(out_List, GPIO.LOW)

	# INSTEAD WE MUST WRITE A FUNCTION THAT TAKES AS INPUT THE PIN TO SET LOW
	# WE THEN SET THE PIN LOW AND CALL A FUNCTION TO WAIT AND REPEAT
	return;

def wait():
	print("Waiting 1 second")
	time.sleep(1)
	return;

def clean():
	print("Cleaning GPIO")
	GPIO.cleanup()
	return;

def main():
	print("Program Running...")

	clean()
	config()
	wait()

	return;

main()











