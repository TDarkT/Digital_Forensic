import cv2 as cv
import numpy as np
import sys

forme1 = cv.imread("./forme1.png",cv.IMREAD_GRAYSCALE)
forme3 = cv.imread("./LabWork_3/forme3.png", cv.IMREAD_GRAYSCALE)
#lena = cv.imread("./LabWork_3/lena.png", cv.IMREAD_GRAYSCALE)

ret1, forme1_bin = cv.threshold(forme1,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
ret2, forme3_bin = cv.threshold(forme3,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
#ret, lena_bin = cv.threshold(lena,125,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imwrite("./LabWork_3/Result/forme1_bin_otsu.png", forme1_bin)
cv.imwrite("./LabWork_3/Result/forme3_bin_otsu.png", forme3_bin)
#cv.imwrite("./LabWork_3/Result/lena_bin_otsu.png", lena_bin)

print("threshold value for forme1: %d " % ret1)
print("threshold value for forme3: %d " % ret2)

cv.imshow("Binary threshold",forme1_bin)
k = cv.waitKey(0)
if k == ord("q"):
    sys.exit()
