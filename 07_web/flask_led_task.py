from flask import Flask
import RPi.GPIO as GPIO

LED_PIN1 = 5
LED_PIN2 = 6

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!</p>
    <a href="/red/led/on">RED LED ON</a>
    <a href="/red/led/off">RED LED OFF</a>
    <a href="/blue/led/on">BLUE LED ON</a>
    <a href="/blue/led/off">BLUE LED OFF</a>
'''


@app.route("/<color>/led/<op>")
def redled_op(op,color):
    if op == "on":
        if color == "red":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return '''
        <p>RED LED ON</p>
        <a href="/">Go Home</a>
        '''
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return '''
        <p>BLUE LED ON</p>
        <a href="/">Go Home</a>
        '''
    elif op == "off":
        if color == "red":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return '''
        <p>RED LED OFF</p>
        <a href="/">Go Home</a>
        '''
        elif color == "blue":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return '''
        <p>BLUE LED OFF</p>
        <a href="/">Go Home</a>
        '''


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()