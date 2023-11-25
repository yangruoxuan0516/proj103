from flask import Flask, render_template
import motor
app = Flask(__name__)

motor = motor.motorDriver()

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/forward")
def forward():
    motor.forward()
    going="going forward"
    return render_template('index.html',going=going)  

@app.route("/backward")
def backward():
    going = "going backward"
    return render_template('index.html', going=going)

@app.route("/left")
def left():
    going = "going left"
    return render_template('index.html', going=going)

@app.route("/right")
def right():
    going = "going right"
    return render_template('index.html', going=going)

@app.route("/stop")
def stop():
    going = "stopped"
    return render_template('index.html', going=going)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
