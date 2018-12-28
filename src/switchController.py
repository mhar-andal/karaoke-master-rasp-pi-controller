# External Modules
import RPi.GPIO as GPIO
import time




def config():

	# follows pin numbers listed on header P1
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin_number, GPIO.OUT)

	# could optionally be GPIO.LOW / 0 / false
	# out_List = {11,12}
	pin_number = 11
	GPIO.output(pin_number, GPIO.LOW)

	# WE CANNOT DO THIS SINCE WE CANNOT TRIGGER MULTIPLE AT THE SAME TIME 
	# GPIO.output(out_List, GPIO.LOW)

	# INSTEAD WE MUST WRITE A FUNCTION THAT TAKES AS INPUT THE PIN TO SET LOW
	# WE THEN SET THE PIN LOW AND CALL A FUNCTION TO WAIT AND REPEAT
	return

def wait():
	time.sleep(0.075)
	return

def clean():
	GPIO.cleanup()
	return

def main():
	print("Program Running...")

	config()
	wait()
	clean()
	while(1):
		print("Hello")










