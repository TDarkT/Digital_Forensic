import cv2 as cv
import numpy as np
import sys

forme1 = cv.imread("./forme1.png",cv.IMREAD_GRAYSCALE)
house8 = cv.imread("./LabWork_3/house8.png", cv.IMREAD_GRAYSCALE)
femme = cv.imread("./LabWork_3/femme.png", cv.IMREAD_GRAYSCALE)

ret, forme1_bin = cv.threshold(forme1,100,255,cv.THRESH_BINARY)
ret, house8_bin = cv.threshold(house8,120,255,cv.THRESH_BINARY)
ret, femme_bin = cv.threshold(femme,125,255,cv.THRESH_BINARY)

cv.imwrite("./LabWork_3/Result/forme1_bin.png", forme1_bin)
cv.imwrite("./LabWork_3/Result/house8_bin.png", house8_bin)
cv.imwrite("./LabWork_3/Result/femme_bin.png", femme_bin)


cv.imshow("Binary threshold",femme_bin)
k = cv.waitKey(0)
if k == ord("q"):
    sys.exit()
