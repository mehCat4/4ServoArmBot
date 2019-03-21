import RPi.GPIO as GPIO
import time

# Variables here
servoPINBase = 17
servoPINPinch = ""
servoPINLift = ""
sevoPINForward = ""
yes_no = ""

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPINBase, GPIO.OUT)

p = GPIO.PWM(servoPINBase, 50)      # GPIO 17 for PWM with 50Hz
p.start(2.5)                # Init
try:
    while True:
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(10)
        time.sleep(0.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
        p.ChangeDutyCycle(5)
        time.sleep(0.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(0.5)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
