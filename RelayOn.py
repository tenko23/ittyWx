import RPi.GPIO as GPIO
from datetime import datetime

def turn_on_relay():
    GPIO.setmode(GPIO.BCM)
    RELAIS_1_GPIO = 17  #Please make sure your GPIO number is correct.
    GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    print("\nPrinting alert(s) on Teletype at",datetime.now().time(), "\n")