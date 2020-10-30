import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cadastre2 = cv.imread("./LabWork_3/cadastre2.png",cv.IMREAD_GRAYSCALE) # convert image to grayscale

ret2, cadastre2_bin = cv.threshold(cadastre2, 0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)

kernel = np.ones((11,11), np.uint8)

thick_wall = cv.morphologyEx(cadastre2_bin, cv.MORPH_CLOSE, kernel)

cv.imwrite("./LabWork_3/Result/cadastre2_thick.png", thick_wall)

thin_wall = cv.bitwise_xor(cadastre2_bin,thick_wall,thick_wall)
thin_wall = cv.bitwise_not(thin_wall)
cv.imwrite("./LabWork_3/Result/cadastre2_thin.png", thin_wall)
