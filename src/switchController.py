import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

# could optionally be GPIO.LOW / 0 / false
# out_List = {11,12}
GPIO.output(12, GPIO.LOW)

GPIO.output(out_List, GPIO.LOW)





