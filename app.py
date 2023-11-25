from flask import Flask, render_template, Response
import cv2
import time
import atexit
import motor.motor as motor
import aruco.detect_aruco as detect
import reach_aruco as reach

app = Flask(__name__)
Motor = motor.MotorDriver()
cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
@app.route('/')
def manual():
    return render_template('manual.html')

def video_result():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = detect.detect_aruco(frame)
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # This step is necessary because the Flask Response object expects
            # a byte-like object for streaming.
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
@app.route('/video')
def video():
    return Response(video_result(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/forward")
def forward():
    motor.forward(Motor,100)
    going="going forward"
    return render_template('manual.html',going=going)  

@app.route("/backward")
def backward():
    motor.backward(Motor,100)
    going = "going backward"
    return render_template('manual.html', going=going)

@app.route("/left")
def left():
    motor.left(Motor,100)
    going = "going left"
    return render_template('manual.html', going=going)

@app.route("/right")
def right():
    motor.right(Motor,100)
    going = "going right"
    return render_template('manual.html', going=going)

@app.route("/stop")
def stop():
    motor.stop(Motor)
    going = "stopped"
    return render_template('manual.html', going=going)

@app.route("/auto",methods=['GET'])
def auto():
    time.sleep(0.5)
    _, image = cap.read()
    reach.reach_aruco(image)
    return render_template('auto.html')

atexit.register(stop)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)



            
