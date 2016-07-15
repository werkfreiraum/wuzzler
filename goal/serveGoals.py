#!/usr/bin/python
from flask import Flask
import RPi.GPIO as GPIO

PIN_RED = 14
PIN_BLU = 15

PIN_RESET = 18

BOUNCE_TIME = 2000

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RED, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BLU, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_RESET, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

app = Flask(__name__)

score = [0, 0]

# str(GPIO.input(14)) + str(GPIO.input(15)) + str(GPIO.input(18))

def goal(channel):
    print("GOAL" + str(channel))
    if channel == PIN_RED:
        score[0] += 1
    if channel == PIN_BLU:
        score[1] += 1

def reset(channel):
    score[0] = 0
    score[1] = 0
	

GPIO.add_event_detect(PIN_RED, GPIO.FALLING, callback=goal, bouncetime=BOUNCE_TIME)
GPIO.add_event_detect(PIN_BLU, GPIO.FALLING, callback=goal, bouncetime=BOUNCE_TIME)

GPIO.add_event_detect(PIN_RESET, GPIO.FALLING, callback=reset, bouncetime=BOUNCE_TIME)

@app.route("/")
def scoreOutput():
    return '{: 2d}{: 2d}'.format(*score)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
