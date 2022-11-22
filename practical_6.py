# Write a program to implement linear and nonlinear noise
# smoothing on suitable image or sound signal.

# ImageFilter for using filter() function
from PIL import Image, ImageFilter

# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open(r"./logo.jpg")

# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
image = image.filter(ImageFilter.GaussianBlur)

# Displaying the image
image.show() 

# Median filter ---------------------------

# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter
	
# creating a image object
im1 = Image.open(r"./logo.jpg")
# applying the median filter
im2 = im1.filter(ImageFilter.MedianFilter(size = 3))
	
im2.show()

# Non Linear – Mode Filter ---------------------------------

# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter
# creating a image object
im1 = Image.open(r"./logo.jpg")
# applying the mode filter
im2 = im1.filter(ImageFilter.ModeFilter(size = 3))
im2.show()


