from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN1 = 12
LED_PIN2 = 21

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

@app.route("/")
def hello():
    return render_template("led_task.html")


@app.route("/<color>/led/<op>")
def led_op(op,color):
    if color == "red":
        if op == "on":
            GPIO.output(LED_PIN1, GPIO.HIGH)
            return "RED LED ON"
        elif op == "off":
            GPIO.output(LED_PIN1, GPIO.LOW)
            return "RED LED OFF"
    elif color == "blue":
        if op == "on":
            GPIO.output(LED_PIN2, GPIO.HIGH)
            return "BLUE LED ON"
        elif op == "off":
            GPIO.output(LED_PIN2, GPIO.LOW)
            return "BLUE LED OFF"
    else:
        return "Error"


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()