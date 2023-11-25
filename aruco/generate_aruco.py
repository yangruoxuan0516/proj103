import numpy as np
import cv2

ARUCO_DICT = {
    "DICT_5X5_50": cv2.aruco.DICT_5X5_50
}
# "NXN" is bit*bit
# the last number is the number of id we can generate

arucoDict = cv2.aruco.getPredefinedDictionary(ARUCO_DICT["DICT_5X5_50"])
# The cv2.aruco.Dictionary_get function returns
# all information OpenCV needs to draw our ArUco tags.

tag = np.zeros([300,300,1],dtype="uint8")
# allocate memory for a 300x300x1 grayscale image.

cv2.aruco.generateImageMarker(arucoDict, 0, 300, tag, 1)
# 2nd - id
# 3rd - corresponding to tag
# 4th - remember to add the array!!
# 5th - width of the edge, unit:bit, in dict, the "N" in "NXN" is bit too

tag_ = [250 for i in range(250000)]
tag_ = np.reshape(tag_,(500,500,1))
for i in range(100,400):
    for j in range(100,400):
        tag_[i][j] = tag[i-100][j-100]
tag_ = tag_.astype(np.uint8)
cv2.imwrite("./ABOUT_aruco/an_ArUCo.png",tag_)
cv2.imshow("ArUCo",tag_)
cv2.waitKey(0)