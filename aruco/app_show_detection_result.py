from flask import Flask, render_template, Response
import cv2
import detect_aruco

app = Flask(__name__)
cap = cv2.VideoCapture(0) 

@app.route('/')
def index():
    return render_template('index.html')


def video_result():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame,_,_ = detect_aruco.detect_aruco(frame)
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # This step is necessary because the Flask Response object expects
            # a byte-like object for streaming.
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video')
def video():
    return Response(video_result(), mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
