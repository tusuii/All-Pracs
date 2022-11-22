# Write program to demonstrate the following aspects of signal on sound/image data
#     1. Convolution operation
#     2. Template Matching

# 1.Blurring using convolution operation Box Blurring 

# Importing the OpenCV, Numpy and Mat libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image from the disk using cv2.imread() function
# Showing the original image using matplotlib library function plt.imshow()
img = cv2.imread('g4g.png')
plt.imshow(img)
plt.show()

# Kernel for box blur filter
# It is a unity matrix which is divided by 9
box_blur_ker = np.array([[0.1111111, 0.1111111, 0.1111111],[0.1111111, 0.1111111, 0.1111111],[0.1111111, 0.1111111, 0.1111111]])

# Applying Box Blur effect
# Using the cv2.filter2D() function
# src is the source of image(here, img)
# ddepth is destination depth. -1 will mean output image will have same depth as input image
# kernel is used for specifying the kernel operation (here, box_blur_ker)
Box_blur = cv2.filter2D(src=img, ddepth=-1, kernel=box_blur_ker)

# Showing the box blur image using matplotlib library function plt.imshow()
plt.imshow(Box_blur)
plt.show()


# 2.Template matching

import cv2
import numpy as np

# Read the main image
img_rgb = cv2.imread('mainimage.jpg')

# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Read the template
template = cv2.imread('template', 0)

# Store width and height of template in w and h
w, h = template.shape[::-1]

# Perform match operations.
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.8

# Store the coordinates of matched area in a numpy array
loc = np.where(res >= threshold)

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Show the final image with the matched area.
cv2.imshow('Detected', img_rgb)
