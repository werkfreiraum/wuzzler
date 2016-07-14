#!/usr/bin/python
from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

app = Flask(__name__)

@app.route("/")
def hello():
    return "P" + str(GPIO.input(14)) + str(GPIO.input(15)) + str(GPIO.input(18))

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
