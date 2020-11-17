# -*- coding: utf-8 -*-
# @Time    : 2020-11-16 19:33
# @Author  : Inger

'''
Cut the pipe from raw images and resize it to 64*64.
'''


import cv2
import os
import os.path as osp
import numpy as np

input_path = "/Users/inger/underground/longgang"
output_path = "/Users/inger/underground/datasets/"

def image_process():

    for file in os.listdir(input_path):
        print("Processing " + file)
        filename = osp.join(input_path, file)
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)



        ret, image_bin = cv2.threshold(img, 32, 255,
                                               cv2.THRESH_BINARY)
        dst = cv2.bitwise_not(image_bin)
        cnts, hi = cv2.findContours(dst.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            # 如果当前轮廓的面积太少，认为可能是噪声，直接忽略掉
            if cv2.contourArea(c) < 1000:
                continue
            print(cv2.contourArea(c))

            # 根据物体轮廓计算出外切矩形框
            (x0, y0, w, h) = cv2.boundingRect(c)
            align = max(w, h)
            print(x0, y0, align)
            pipe = img[x0: x0+align+1, y0: y0+align+1]
            cv2.resize(pipe, (64, 64), interpolation = cv2.INTER_AREA)
            cv2.imshow("img",pipe)
            cv2.imwrite(osp.join(output_path, file), pipe)
            print(file + " Save Successfully!")




def make_neg(path):
    image = cv2.imread(path)
    image = cv2.resize(image, (640,480), interpolation=cv2.INTER_AREA)
    k = 0
    rows, cols, = image.shape[0:2]  # 获得行数和列数
    r1, r2 = [0, 64]  # 初始化r1, r2
    while r2 <= rows:
        c1, c2 = [0, 64]  # 每循环一次，要重新给c1,c2赋值
        while c2 <= cols:
            # 截取图片
            img = image[r1: r2 + 1, c1: c2 + 1]
            # 把截图的图片保存到文件中
            print("saving " + str(k))
            cv2.imwrite(output_path + 'non-pipe/' + str(k) + '.jpg', img)
            k, c1, c2 = [k + 1, c1 + 64, c2 + 64]  # 更新值
        r1, r2 = [r1 + 64, r2 + 64]  # 更新值
    print('finish')

# path = "./pic/pipe/010.png"
# make_neg(path)
