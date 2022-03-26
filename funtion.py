# -*- coding:UTF-8 -*-
import cv2
import numpy as np

kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((5,5),np.uint8)


img = cv2.imread('color.jpg')
img = cv2.resize(img, (0,0), fx=1.5,fy=1.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉換成灰階的圖片

# blur = cv2.GaussianBlur(img, (15,15), 10) #轉換成模糊

canny = cv2.Canny(img, 200, 250) #邊緣檢測

dileate = cv2.dilate(canny, kernel1, iterations=1 )#膨脹邊緣效果

erode = cv2.erode(dileate,kernel2, iterations=1) #侵蝕效果


# cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dileate)
cv2.imshow('erode',erode)
cv2.waitKey(0)