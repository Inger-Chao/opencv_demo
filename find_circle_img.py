# -*- coding: utf-8 -*-
# @Time    : 2020-11-08 16:23
# @Author  : Inger

import numpy as np
import cv2
import matplotlib.pyplot as plt


#
# def empty(a):
#     pass
#
# cv2.namedWindow("Parameters", cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
# cv2.resizeWindow("Parameters",640,240)
# cv2.createTrackbar("Threshold1","Parameters",23,255,empty)
# cv2.createTrackbar("Threshold2","Parameters",145,255,empty)

def showMultImg(imgs):
    for i in range(1, len(imgs)):
        plt.subplot(2, 2, i)
        plt.imshow(imgs[i-1])
        plt.xticks([])
        plt.yticks([])
    plt.show()

def getCircle(img ,output):
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 260,
                               param1=30, param2=65, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle in the image
            # corresponding to the center of the circle
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            # time.sleep(0.5)
            print("Column Number: ")
            print(x)
            print("Row Number: ")
            print(y)
            print("Radius is: ")
            print(r)


img = cv2.imread('/Users/inger/underground/789-779-line/00000085.jpg')
output = img.copy()
imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
# threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
# threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
imgCanny = cv2.Canny(imgGray, 6, 136)
kernel = np.ones((5, 5))
imgDil = cv2.dilate(imgCanny, kernel, iterations=1)
getCircle(imgDil, output)

cv2.namedWindow("result", 0)
cv2.resizeWindow("result", 640, 480)
cv2.imshow("result", output)
cv2.waitKey(0)
showMultImg([img, imgCanny, imgDil])
cv2.destroyAllWindows()