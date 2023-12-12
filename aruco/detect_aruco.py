import cv2
import argparse

ap= argparse.ArgumentParser()
ap.add_argument("-t","--type", type=str, default="DICT_6X6_50", help="type of ArUCo tag to detect")
args=vars(ap.parse_args())

ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT[args["type"]])


# arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
# The cv2.aruco.Dictionary_get function returns
# all information OpenCV needs to draw our ArUco tags.
arucoParams = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)


def detect_aruco(image):
	(corners, ids, rejected) = detector.detectMarkers(image)
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
			# draw the bounding box of the ArUCo detection
			cv2.line(image, topLeft, topRight, (0, 255, 0), 2)
			cv2.line(image, topRight, bottomRight, (0, 255, 0), 2)
			cv2.line(image, bottomRight, bottomLeft, (0, 255, 0), 2)
			cv2.line(image, bottomLeft, topLeft, (0, 255, 0), 2)
		    # compute and draw the center (x, y)-coordinates of the ArUco marker
			cX = int((topLeft[0] + bottomRight[0]) / 2.0)
			cY = int((topLeft[1] + bottomRight[1]) / 2.0)
			cv2.circle(image, (cX, cY), 4, (0, 0, 255), -1)
			# draw the ArUco marker ID on the image
			cv2.putText(image, str(markerID),(cX, cY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
			# coordinate of corners
			cv2.putText(image, str(topLeft),(topLeft[0]-80, topLeft[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(image, str(topRight),(topRight[0], topRight[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(image, str(bottomLeft),(bottomLeft[0]-80, bottomLeft[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(image, str(bottomRight),(bottomRight[0], bottomRight[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			# length of edges
			cv2.putText(image, str(bottomLeft[1]-topLeft[1]),(topLeft[0]-45, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(image, str(bottomRight[1]-topRight[1]),(topRight[0]+15, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(image, str(topRight[0]-topLeft[0]),(cX-15, topLeft[1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
			cv2.putText(image, str(bottomRight[0]-bottomLeft[0]),(cX-15, bottomLeft[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		    # distance
			distance = int(21000/(bottomRight[1]-topRight[1]+bottomLeft[1]-topLeft[1]))
			cv2.putText(image, "The ArUCo is about "+str(distance)+" cm from me",(15,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			# left / right
			_,width,_ = image.shape
			if cX < width*0.4:
				direction = 1
				cv2.putText(image, "It is a little bit to my left",(15,65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			elif cX > width*0.6:
				direction = 3
				cv2.putText(image, "It is a little bit to my right",(15,65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			else:
				direction = 2	
				cv2.putText(image, "It is right in front of me",(15,65), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			# show the output image
			return image,direction,distance
	return image,0,None


# -- test using picture -- #
# image = cv2.imread("./ABOUT_aruco/an_ArUCo.png")
# cv2.imshow("image",image)
# cv2.waitKey(0)
# image = detect_aruco(image)
# cv2.imshow("Image", image)
# cv2.waitKey(0)


# -- test using camera video -- #
# # Create a VideoCapture object to access the camera
# cap = cv2.VideoCapture(0)  # 0 for default camera, change the index if you have multiple cameras
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # Get the dimensions of the image using the shape
#     height, width, _ = frame.shape
#     print(height," ",width)
#     frame = detect_aruco(frame)
#     cv2.imshow('Camera Feed', frame)
#     # Press 'q' to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # Release the VideoCapture and close the window
# cap.release()
# cv2.destroyAllWindows()


