# Write program to implement point/pixel intensity transformations such as
#     1. Log and Power-law transformations
#     2. Contrast adjustments
#     3. Histogram equalization
#     4. Thresholding, and halftoning operations


import cv2
import numpy as np

# Open the image.
img = cv2.imread('logo.jpg')

# Apply log transform.
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

# Specify the data type.
log_transformed = np.array(log_transformed, dtype = np.uint8)

# Save the output.
cv2.imwrite('log_transformed.jpg', log_transformed)



# Power-law transformations   part 2
import cv2
import numpy as np

# Open the image.
img = cv2.imread('sample.jpg')

# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
	
	# Apply gamma correction.
	gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')

	# Save edited images.
	cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)


# 3. Histogram equalization

from PIL import Image, ImageEnhance

#read the image
im = Image.open("g4g.png")

#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)
factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

factor = 0.5 #decrease constrast
im_output = enhancer.enhance(factor)
im_output.save('less-contrast-image.png')

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('more-contrast-image.png')


# 3. Histogram equalization

# import Opencv
import cv2

# import Numpy
import numpy as np

# read a image using imread
# img = cv2.imread(\'F:\\do_nawab.png\', 0)
img = cv2.imread(g4g.png, 0)
# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv2.imshow(equalizeHist_out.jpg, res)



#     4. Thresholding, and halftoning operations

# Python program to illustrate
# simple thresholding type on an image
	
# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv2.imread('logo.jpg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# all pixels value above 120 will
# be set to 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

# the window showing output images
cv2.imshow('Binary Threshold', thresh1)
