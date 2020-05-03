import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)

def turn_off_relay():
    GPIO.setmode(GPIO.BCM)
    RELAIS_1_GPIO = 17  #Please make sure your GPIO number is correct.
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    print("\nPrintout complete on Teletype at",datetime.now().time(), "\n")
    GPIO.cleanup()