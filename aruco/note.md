# [Generating ArUco markers with OpenCV and Python](https://pyimagesearch.com/2020/12/14/generating-aruco-markers-with-opencv-and-python/)
## AprilTag
- 基准标记(Fiducial marker): reference objects
- The computer vision software
  - takes the input image
  - detects the fiducial marker
  - performs some operation based on the type of marker and where the marker is located in the input image
- AprilTags are a specific type of fiducial marker
- The black border surrounding the marker makes it easier for computer vision and image processing algorithms to detect the AprilTags
## ArUco dictionary
- ArUco dictionary specifies the type of ArUco marker we are generating and detecting
- There are 21 different ArUco dictionaries built into the OpenCV library
- The majority of these dictionaries follow a specific naming convention, cv2.aruco.DICT_NxN_M, with an NxN size followed by an integer value M 
  - The NxN value is the 2D bit size of the ArUco marker. For example, for a 6×6 marker we have a total of 36 bits
  - The integer M following the grid size specifies the total number of unique ArUco IDs that can be generated with that dictionary
- How do you decide on which ArUco marker dictionary you want to use?
  - Pick a dictionary that has the bare minimum number of IDs you need — don’t take more than what you actually need.
  - Look at your input image/video resolution size. If you have a large grid but a low resolution input, then the marker may be undetectable (or may be misread).
  - A larger NxN grid size, balanced with a low number of unique ArUco IDs such that the inter-marker distance can be used to correct misread markers.

# [Detecting ArUco markers with OpenCV and Python](https://pyimagesearch.com/2020/12/21/detecting-aruco-markers-with-opencv-and-python/)
- Inputting image / video
- Specifying ArUco dictionary
- Creating the parameters to the ArUco detector (which is typically just a single line of code using the default values)
- Applying the function to actually detect the ArUco markers



## [module 'cv2.aruco' has no attribute 'xxx'.](https://blog.csdn.net/weixin_41837701/article/details/129256430)