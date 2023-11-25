from flask import Flask, render_template, Response
import cv2
import time
import atexit
import motor.motor as motor
import aruco.detect_aruco as detect

app = Flask(__name__)
Motor = motor.MotorDriver()
cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
@app.route('/')
def manual():
    return render_template('manual.html')

def turn_left_a_little():
    motor.left(Motor,40)
    time.sleep(0.2)
    motor.stop(Motor)
    time.sleep(3)

def turn_right_a_little():
    motor.right(Motor,40)
    time.sleep(0.2)
    motor.stop(Motor)
    time.sleep(3)

def go_forward_a_little():
     motor.forward(Motor,40)
     time.sleep(0.2)
     motor.stop(Motor)
     time.sleep(3)

def reach_aruco(direction,distance,found,left):
    if direction:
        found = True            
        if direction == 1:
            turn_left_a_little()
            left = False
        elif direction == 3:
            turn_right_a_little()
            left = True
        elif direction == 2 and distance <= 25:
            go_forward_a_little()
    elif found:
        if left:
            turn_left_a_little()
            left = False
        else:
            turn_right_a_little()
            left = True
    else:
        turn_left_a_little()


def video_result():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame,_,_ = detect.detect_aruco(frame)
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # This step is necessary because the Flask Response object expects
            # a byte-like object for streaming.
            with app.app_context():
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            

def video_result_auto():
    found = False
    left = True # need to turn left
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame,direction,distance = detect.detect_aruco(frame)
            if distance:
                if distance <= 25:
                    break
            reach_aruco(direction,distance,found,left)
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # This step is necessary because the Flask Response object expects
            # a byte-like object for streaming.
            with app.app_context():
                yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


            
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

@app.route("/auto")
def auto():
    return Response(video_result_auto(), mimetype='multipart/x-mixed-replace; boundary=frame')

atexit.register(stop)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)



            
