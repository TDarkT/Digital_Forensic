import cv2 as cv
import sys


img = cv.imread(("./football.jpeg"))

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
player1 = img[75:240, 92:187]
cv.imshow("Player1", player1)
cv.imwrite("Player1.png", player1)
ball = img[198:222,212:237]
cv.imshow("Ball", ball)
cv.imwrite("ball.png", ball)

player2 = img[90:235,250:334]
cv.imshow("Player2", player2)
cv.imwrite("Player2.png", player2)
k = cv.waitKey(0)

