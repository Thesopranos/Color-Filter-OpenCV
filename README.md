# Color Filter using OpenCV
This script captures video from the default camera and applies a color filter to it using the OpenCV library. The filter is based on the HSV color space and the user can adjust the lower and upper limits of H, S, and V values using trackbars in the "color" window.
# In-script Image
![Screenshot_1](https://user-images.githubusercontent.com/68299931/213162763-835bb12b-936b-4544-9e19-9a1121cececd.png)

# Requirements
Python 3  
OpenCV
Numpy
# Usage
Run the script python color_filter.py  
The video from the default camera will be displayed in a window named "Camera".  
Use the trackbars in the "color" window to adjust the lower and upper limits of H, S, and V values.  
Press "q" to exit the script.  
# Result
The original video is displayed in the "Camera" window.  
The "mask" window shows the pixels that are within the specified range of H, S, and V values.  
The "sonuc" window shows the result of applying the mask to the original video.  
# Note
The H values are divided by 2 because OpenCV uses a range of 0-180 for H in the HSV color space, while the trackbar is created using a range of 0-359.
The default camera index is 0, if you wish to use different camera you should change the index number in cap = cv2.VideoCapture(0)
