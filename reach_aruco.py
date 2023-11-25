import cv2
import motor.motor as motor
import aruco.detect_aruco as detect
import time

arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
arucoParams = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
Motor = motor.MotorDriver()

def reach_aruco(image):
    found = False
    left = True # need to turn left
    while True:
        [direction,distance] = detect_aruco(image)
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
            else:
                break
        elif found:
            if left:
                turn_left_a_little()
                left = False
            else:
                turn_right_a_little()
                left = True
        else:
            turn_left_a_little()


def detect_aruco(image):
    (corners, ids, _) = detector.detectMarkers(image)
    # Each markerCorner is represented by a list of four (x, y)-coordinates
    # (top-left, top-right, bottom-right, and bottom-left)
    if len(corners) > 0:
        ids = ids.flatten()
	    # loop over the detected ArUCo corners
        for (markerCorner, markerID) in zip(corners, ids):
		    # extract the marker corners (which are always returned in
		    # top-left, top-right, bottom-right, and bottom-left order)
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners
		    # convert each of the (x, y)-coordinate pairs to integers
            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            distance = int(21000/(bottomRight[1]-topRight[1]+bottomLeft[1]-topLeft[1]))
            _ , width, _ = image.shape
            if cX < width*0.4:
                direction = 1
            elif cX > width*0.6:
                direction = 3
            else:
                direction = 2
            return [direction,distance]
    return [0,None]
    
def turn_left_a_little():
    motor.left(Motor,45)
    time.sleep(0.05)

def turn_right_a_little():
    motor.right(Motor,45)
    time.sleep(0.05)

def go_forward_a_little():
     motor.forward(Motor,45)
     time.sleep(0.05)


    


