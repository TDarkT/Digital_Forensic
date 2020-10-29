import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

forme1 = cv.imread("./forme1.png",cv.IMREAD_GRAYSCALE)
house8 = cv.imread("./LabWork_3/house8.png", cv.IMREAD_GRAYSCALE)
femme = cv.imread("./LabWork_3/femme.png", cv.IMREAD_GRAYSCALE)
forme3 = cv.imread("./LabWork_3/forme3.png", cv.IMREAD_GRAYSCALE)

#Get the histogram of forme1.png
#plt.hist(house8.ravel(),256,[0,256])
#plt.show()
#Get the histogram of house8.png
#plt.hist(house8.ravel(),256,[0,256])
#plt.show()
#Get the histogram of femme.png
#plt.hist(femme.ravel(),256,[0,256])
#plt.show()
#Get the histogram of femme.png
#plt.hist(house8.ravel(),256,[0,256])
#plt.show()

ret, forme1_bin = cv.threshold(forme1,127,255,cv.THRESH_BINARY) # optimal threshold based on histogram: 127
ret, house8_bin = cv.threshold(house8,110,255,cv.THRESH_BINARY) # optimal threshold based on histogram: 110 
ret, femme_bin = cv.threshold(femme,110,255,cv.THRESH_BINARY)
ret, forme3_bin = cv.threshold(forme3,130,255,cv.THRESH_BINARY) # optimal threshold based on histogram: 110 

cv.imwrite("./LabWork_3/Result/forme1_binwithhist.png", forme1_bin)
cv.imwrite("./LabWork_3/Result/house8_binwithhist.png", house8_bin)
cv.imwrite("./LabWork_3/Result/femme_binwithhist.png", femme_bin)
cv.imwrite("./LabWork_3/Result/forme3_binwithhist.png", forme3_bin)
