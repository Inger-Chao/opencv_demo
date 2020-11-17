# -*- coding: utf-8 -*-
# @Time    : 2020-11-09 12:50
# @Author  : Inger

import cv2
import numpy as np


def nothing(x):
    pass

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

def mythreshold(imagepath):
    # open image
    image_org = cv2.imread(imagepath)

    cv2.namedWindow("image")
    cv2.resizeWindow("image", 640, 480)
    cv2.createTrackbar("threshold1", "image", 23, 255, nothing)

    height, width = image_org.shape[:2]
    # 缩小图片
    size = (int(width * 0.5), int(height * 0.5))
    image_org = cv2.resize(image_org, size, interpolation=cv2.INTER_AREA)

    blured = cv2.GaussianBlur(image_org, (7,7), 1)

    # transe image to gray
    image_gray = cv2.cvtColor(blured, cv2.COLOR_RGB2GRAY)


    while True:
        mythreshold = cv2.getTrackbarPos("threshold1", "image")
        ret, image_bin = cv2.threshold(image_gray, mythreshold, 255,
                                       cv2.THRESH_BINARY)


        cv2.imshow("image", image_bin)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


def main():
    path = "/Users/inger/underground/longgang/00000057.jpg"
    mythreshold(path)


if __name__ == '__main__':
    main()