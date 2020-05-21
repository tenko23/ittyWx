import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#This script is for manually turning off the 5v relay, connected to your Raspberry Pi.

GPIO.setwarnings(False)
 
RELAIS_1_GPIO = 17  #Please make sure your GPIO number is correct.
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
GPIO.cleanup()