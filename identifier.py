import cv2 as cv
import sys
 
img = cv.imread("12.png")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow('sample image',img)
 
cv.waitKey(0) # waits until a key is pressed

cv.destroyAllWindows() # destroys the window showing image


