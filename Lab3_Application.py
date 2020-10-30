import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cadastre1 = cv.imread("./LabWork_3/cadastre1.png",cv.IMREAD_GRAYSCALE) # convert image to grayscale

plt.hist(cadastre1.ravel(),256,[0,256])
plt.show()
# Show histogram to pick optimal threshold value:170

ret1, cadastre1_bin = cv.threshold(cadastre1,170,255,cv.THRESH_BINARY)

cv.imwrite("./LabWork_3/Result/cadastre1_bin.png", cadastre1_bin)

cv.imshow("Text extraction",cadastre1_bin)
k = cv.waitKey(0)
if k == ord("q"):
    sys.exit()
