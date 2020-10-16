import cv2 as cv
import sys

img = cv.imread("logo-usth.png")
# Extract RGB channel

red_channel = img[:,:,2]
blue_channel = img[:,:,0]
green_channel = img[:,:,1]
cv.imwrite("Red.png", red_channel)
cv.imwrite("Green.png", green_channel)
cv.imwrite("Blue.png", blue_channel)

ret,red_mask = cv.threshold(red_channel,127,255,cv.THRESH_BINARY)
cv.imwrite("Red_mask.png", red_mask)
ret,blue_mask = cv.threshold(blue_channel,127,255,cv.THRESH_BINARY)
cv.imwrite("Blue_mask.png", blue_mask)
imS = cv.resize(blue_mask, (960, 540)) 
cv.imshow("mask", imS)
k = cv.waitKey(0)
if k == ord("q"):
    sys.exit()