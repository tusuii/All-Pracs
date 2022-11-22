# Write a program to apply various enhancements on images
# using image derivatives by implementing Gradient and Laplacian
# operations.

# Using Laplacian operator

# importing required libraries
import mahotas
import numpy as np
from pylab import gray, imshow, show
import os
import matplotlib.pyplot as plt

# loading image
img = mahotas.imread('g4g.png')


# filtering image
img = img[:, :, 0]

print("Image")

# showing image
imshow(img)
show()

# applying 2D Laplacian filter
new_img = mahotas.laplacian_2D(img)


# showing image
print("2D Laplacian filter")
imshow(new_img)
show()


# using Gradient operator


# Python program to  Edge detection
# using OpenCV in Python
# using Sobel edge detection
# and laplacian method
import cv2
import numpy as np

img = cv2.imread("logo_og.png",1)

#Converting image to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Creating Prewitt filter
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

#Applying filter to the image in both x and y direction
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)

# Taking root of squared sum(np.hypot) from both the direction and displaying the result
prewitt = np.hypot(img_prewitty,img_prewittx)
prewitt = prewitt[:,:,0]
prewitt = prewitt.astype('int')
plt.imshow(prewitt,cmap='gray')

