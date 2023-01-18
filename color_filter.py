# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Open the default camera
cap = cv2.VideoCapture(0)

# Function that does nothing, used for creating the trackbars
def nothing(x):
    pass

# Create a window named "color"
cv2.namedWindow("color")

# Create 6 trackbars for controlling the lower and upper limits of H, S, and V values in HSV color space
cv2.createTrackbar("H1", "color", 0, 359, nothing)
cv2.createTrackbar("H2", "color", 0, 359, nothing)
cv2.createTrackbar("S1", "color", 0, 255, nothing)
cv2.createTrackbar("S2", "color", 0, 255, nothing)
cv2.createTrackbar("V1", "color", 0, 255, nothing)
cv2.createTrackbar("V2", "color", 0, 255, nothing)

# Continuously capture frames
while cap.isOpened():
    # Read a frame
    _, frame = cap.read()
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the current values of the trackbars
    H1 = int(cv2.getTrackbarPos("H1","color")/2) 
    H2 = int(cv2.getTrackbarPos("H2","color")/2) 
    S1 = cv2.getTrackbarPos("S1","color")
    S2 = cv2.getTrackbarPos("S2","color")
    V1 = cv2.getTrackbarPos("V1","color")
    V2 = cv2.getTrackbarPos("V2","color")
    
    # Create numpy arrays for the lower and upper limits
    lower_track = np.array([H1, S1, V1])
    upper_track = np.array([H2, S2, V2])
    
    # Create a mask using the inRange function, which filters out pixels that are not within the specified range
    mask = cv2.inRange(hsv, lower_track, upper_track)
    
    # Perform bitwise and operation to keep only the pixels that are within the specified range
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    # Show the original frame, the mask, and the result
    cv2.imshow("Camera", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("sonuc", res)
    
    # Exit the loop if the user presses "q"
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()